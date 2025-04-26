import math
from bitarray import bitarray
from bitarray.util import ba2int, int2ba
from common.common import (bin_to_hex, hex_to_bin, str_to_bin,
                        add_padding_bytes, block_to_little_endian)

class MD5:
    def __init__(self, text: str = None):
        self.text = text
        self.blocks = []
        self.hash_bin = ""
        self.hash_hex = ""
        self.cache = {}
        self.__shift_constants = [[7, 12, 17, 22] * 4,
                                    [5, 9, 14, 20] * 4,
                                    [4, 11, 16, 23] * 4,
                                    [6, 10, 15, 21] * 4]

        self.__f_functions = [
            lambda x, y, z: (x & y) | (~x & z),
            lambda x, y, z: (x & z) | (y & ~z),
            lambda x, y, z: x ^ y ^ z,
            lambda x, y, z: y ^ (x | ~z)
        ]

        self.__T = self.generate_T()


    def generate_T(self):
        T = []
        for i in range(64):
            T.append(int((2**32) * abs(math.sin(i+1))))
        return T

    def rotate_left(self, x: bitarray, n: int) -> bitarray:
        return ((x << n) | (x >> (32 - n))) & bitarray("1" * 32)

    def add_operator(self, operandA: bitarray, operandB: bitarray) -> bitarray:
        intA = ba2int(operandA)
        intB = ba2int(operandB)
        result = (intA + intB) & 0xFFFFFFFF

        return int2ba(result, length=32)

    def generate_hash(self):
        # Step 1: Convert the input string to a binary representation
        binary_message = str_to_bin(self.text)
        self.cache["message"] = {
            "binary": binary_message.to01(),
            "hex": bin_to_hex(binary_message)
        }
        # Step 2: Pad the message to make its length a multiple of 512 bits
        self.blocks = add_padding_bytes(binary_message)
        self.cache["message_after_padding"] = {
            "binary": ''.join([block.to01() for block in self.blocks]),
            "hex": ''.join([bin_to_hex(block, version=512) for block in self.blocks]),
        }
        # convert blocks to blocks little endian
        self.blocks = [block_to_little_endian(block) for block in self.blocks]
        # Step 3: Initialize the MD5 state variables
        A = hex_to_bin("67452301", 32)
        B = hex_to_bin("EFCDAB89", 32)
        C = hex_to_bin("98badcfe", 32)
        D = hex_to_bin("10325476", 32)
        self.cache["initialize_MD_buffer"] = {
            "little_endian": [
                ba2int(A),
                ba2int(B),
                ba2int(C),
                ba2int(D)
            ],
            "big_endian": [
                bin_to_hex(block_to_little_endian(A)),
                bin_to_hex(block_to_little_endian(B)),
                bin_to_hex(block_to_little_endian(C)),
                bin_to_hex(block_to_little_endian(D))
            ]
        }

        # Step 4: Process each 512-bit block
        k = 0
        for block in self.blocks:
            self.cache[f"block_{k}"] = {
                "words_of_block": {
                    "little_endian": [],
                    "big_endian": []
                },
                "buffers_state": {
                    "little_endian": [],
                    "big_endian": []
                },
                "end_of_block": {
                    "little_endian": [],
                    "big_endian": []
                },
                "intermediate_results": {}
            }
            # Split the block into 16 words of 32 bits each
            words = [block[i:i + 32] for i in range(0, 512, 32)]
            self.addWordsToBlockCache(self.cache[f"block_{k}"]["words_of_block"], words)
            # Initialize the state variables for this block
            A1, B1, C1, D1 = A.copy(), B.copy(), C.copy(), D.copy()

            # Perform the main MD5 algorithm
            for i in range(64):
                interm_res = []
                if i < 16:
                    F = self.__f_functions[0](B1, C1, D1)
                    g = i
                elif i < 32:
                    F = self.__f_functions[1](B1, C1, D1)
                    g = (5 * i + 1) % 16
                elif i < 48:
                    F = self.__f_functions[2](B1, C1, D1)
                    g = (3 * i + 5) % 16
                else:
                    F = self.__f_functions[3](B1, C1, D1)
                    g = (7 * i) % 16

                temp = self.add_operator(F, A1)
                interm_res.append(temp)
                temp = self.add_operator(temp, words[g])
                interm_res.append(temp)
                T, shift = self.__T[i], self.__shift_constants[i // 16][i % 4]
                temp = self.add_operator(temp, int2ba(T, length=32))
                interm_res.append(temp)
                temp = self.rotate_left(temp, shift)
                interm_res.append(temp)
                temp = self.add_operator(temp, B1)
                interm_res.append(temp)

                self.addIntermediateResultsToCache(cache=self.cache[f"block_{k}"][f"intermediate_results"],
                                                   step=i,
                                                   results=interm_res)
                A1, B1, C1, D1 = D1, temp, B1, C1

                self.addNewStateToCache(self.cache[f"block_{k}"]["buffers_state"],
                                        [T, shift, F, A1, B1, C1, D1])

            # Update the state variables
            A = self.add_operator(A, A1)
            B = self.add_operator(B, B1)
            C = self.add_operator(C, C1)
            D = self.add_operator(D, D1)
            self.addEndOfBlockToCache(self.cache[f"block_{k}"]["end_of_block"],
                                      [A, B, C, D])
            k += 1

        # Step 5: Produce the final hash value
        self.hash_bin = A + B + C + D
        self.hash_hex = bin_to_hex(block_to_little_endian(self.hash_bin), version=128)
        return self.hash_hex

    def addIntermediateResultsToCache(self, cache: dict, step: int, results: list[bitarray]) -> None:
        cache[f"step_{step}"] = {
            "little_endian": [],
            "big_endian": []
        }
        for result in results:
            cache[f"step_{step}"]["little_endian"].append(ba2int(result))
            cache[f"step_{step}"]["big_endian"].append(bin_to_hex(block_to_little_endian(result)))

    def addEndOfBlockToCache(self, cache: dict, states: list[bitarray]) -> None:
        for state in states:
            cache["little_endian"].append(ba2int(state))
            cache["big_endian"].append(bin_to_hex(block_to_little_endian(state)))

    def addWordsToBlockCache(self, cache: dict, words: list[bitarray]) -> None:
        for word in words:
            cache["little_endian"].append(ba2int(word))
            cache["big_endian"].append(bin_to_hex(block_to_little_endian(word)))


    def addNewStateToCache(self, cache: dict, states: list):
        T, shift, F, A, B, C, D = states
        bit_array_T = bitarray()
        bit_array_T.frombytes(T.to_bytes(4, byteorder='little'))
        bit_array_shift = bitarray()
        bit_array_shift.frombytes(shift.to_bytes(4, byteorder='little'))

        cache["little_endian"].append([
            bin_to_hex(bit_array_T),
            bin_to_hex(bit_array_shift),
            ba2int(A),
            ba2int(B),
            ba2int(C),
            ba2int(D),
            ba2int(F)
        ])
        cache["big_endian"].append([
            T,
            shift,
            bin_to_hex(block_to_little_endian(A)),
            bin_to_hex(block_to_little_endian(B)),
            bin_to_hex(block_to_little_endian(C)),
            bin_to_hex(block_to_little_endian(D)),
            bin_to_hex(block_to_little_endian(F))
        ])

if __name__ == "__main__":
    text = '''
    Hello world! This is a test message.
    '''
    md5 = MD5(text)
    md5.generate_hash()
    print(md5.cache["block_0"]["end_of_block"]["big_endian"])
    print(md5.cache["block_0"]["buffers_state"]["big_endian"])
    # state = md5.cache["block_0"]["big_endian"]
    # for i in state:
    #     print(i)

