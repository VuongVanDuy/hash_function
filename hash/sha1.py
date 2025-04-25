from bitarray import bitarray
from bitarray.util import ba2int, int2ba
from common.common import (bin_to_hex, hex_to_bin, str_to_bin, add_padding_bytes)

class SHA1:
    def __init__(self, text: str = None):
        self.text = text
        self.blocks = []
        self.hash_bin = ""
        self.hash_hex = ""
        self.cache = {}
        self.__ROL1 = 1
        self.__ROL5 = 5
        self.__ROL30 = 30
        # f functions của SHA1
        self.__f_functions = [
            lambda x, y, z: (x & y) | (~x & z),
            lambda x, y, z: x ^ y ^ z,
            lambda x, y, z: (x & y) | (x & z) | (y & z),
            lambda x, y, z: x ^ y ^ z
        ]

    def rotate_left(self, x: bitarray, n: int) -> bitarray:
        return ((x << n) | (x >> (32 - n))) & bitarray("1" * 32)

    def generate_words(self, block: bitarray) -> list[bitarray]:
        words = []
        for i in range(16):
            word_i = block[i * 32:(i + 1) * 32]
            words.append(word_i)
        for i in range(16, 80):
            word_i = self.rotate_left(words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16], self.__ROL1)
            words.append(word_i)
        return words

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
        self.blocks = add_padding_bytes(binary_message, byteorder="big")
        self.cache["message_after_padding"] = {
            "binary": ''.join([block.to01() for block in self.blocks]),
            "hex": ''.join([bin_to_hex(block, version=512) for block in self.blocks]),
        }

        # Step 3: Initialize the SHA1 state variables
        A = hex_to_bin("67452301", 32)
        B = hex_to_bin("EFCDAB89", 32)
        C = hex_to_bin("98badcfe", 32)
        D = hex_to_bin("10325476", 32)
        E = hex_to_bin("C3D2E1F0", 32)
        self.cache["initialize_SHA_buffer"] = {
            "int_big_endian": [],
            "hex_big_endian": []
        }
        self.addEndOfBlockToCache(self.cache["initialize_SHA_buffer"], [A, B, C, D, E])

        # Step 4: Process each 512-bit block
        k = 0
        for block in self.blocks:
            self.cache[f"block_{k}"] = {
                "words_of_block": {
                    "int_big_endian": [],
                    "hex_big_endian": []
                },
                "buffers_state": {
                    "int_big_endian": [],
                    "hex_big_endian": []
                },
                "end_of_block": {
                    "int_big_endian": [],
                    "hex_big_endian": []
                },
                "intermediate_results": {}
            }

            # Step 4.1: Generate the 80 words
            words = self.generate_words(block)
            self.addWordsToBlockCache(self.cache[f"block_{k}"]["words_of_block"], words)

            # Step 4.2: Initialize the state variables for this block
            A1, B1, C1, D1, E1 = A.copy(), B.copy(), C.copy(), D.copy(), E.copy()
            # self.addNewStateToCache(self.cache[f"block_{k}"]["buffers_state"], [A1, B1, C1, D1, E1])

            # Step 4.3: Process each word
            for i in range(80):
                interm_res = []
                if i < 20:
                    f = self.__f_functions[0](B1, C1, D1)
                    constant = 0x5A827999
                elif i < 40:
                    f = self.__f_functions[1](B1, C1, D1)
                    constant = 0x6ED9EBA1
                elif i < 60:
                    f = self.__f_functions[2](B1, C1, D1)
                    constant = 0x8F1BBCDC
                else:
                    f = self.__f_functions[3](B1, C1, D1)
                    constant = 0xCA62C1D6

                interm_res.append(self.rotate_left(A1, self.__ROL5))

                temp = self.add_operator(self.rotate_left(A1, self.__ROL5), f)
                interm_res.append(temp)
                temp = self.add_operator(temp, E1)
                interm_res.append(temp)
                temp = self.add_operator(temp, words[i])
                interm_res.append(temp)
                temp = self.add_operator(temp, int2ba(constant, length=32))
                interm_res.append(temp)

                self.addIntermediateResultsToCache(cache=self.cache[f"block_{k}"][f"intermediate_results"],
                                                   step=i,
                                                   results=interm_res)

                E1 = D1
                D1 = C1
                C1 = self.rotate_left(B1, self.__ROL30)
                B1 = A1
                A1 = temp

                constant_bin = int2ba(constant, length=32)
                self.addNewStateToCache(self.cache[f"block_{k}"]["buffers_state"],
                                        [constant_bin, A1, B1, C1, D1, E1, f])

            # Step 4.4: Update the SHA1 state variables
            A = self.add_operator(A, A1)
            B = self.add_operator(B, B1)
            C = self.add_operator(C, C1)
            D = self.add_operator(D, D1)
            E = self.add_operator(E, E1)
            self.addEndOfBlockToCache(self.cache[f"block_{k}"]["end_of_block"], [A, B, C, D, E])
            k += 1
        # Step 5: Produce the final hash value
        self.hash_bin = A + B + C + D + E
        self.hash_hex = bin_to_hex(self.hash_bin, version=160)

    def addIntermediateResultsToCache(self, cache: dict, step: int, results: list[bitarray]) -> None:
        cache[f"step_{step}"] = {
            "int_big_endian": [],
            "hex_big_endian": []
        }
        for result in results:
            cache[f"step_{step}"]["int_big_endian"].append(ba2int(result))
            cache[f"step_{step}"]["hex_big_endian"].append(bin_to_hex(result))

    def addEndOfBlockToCache(self, cache: dict, states: list[bitarray]) -> None:
        for state in states:
            cache["int_big_endian"].append(ba2int(state))
            cache["hex_big_endian"].append(bin_to_hex(state))

    def addWordsToBlockCache(self, cache: dict, words: list[bitarray]) -> None:
        for word in words:
            cache["int_big_endian"].append(ba2int(word))
            cache["hex_big_endian"].append(bin_to_hex(word))

    def addNewStateToCache(self, cache: dict, states: list):
        int_big_endian = []
        hex_big_endian = []
        for state in states:
            int_big_endian.append(ba2int(state))
            hex_big_endian.append(bin_to_hex(state))

        cache["int_big_endian"].append(int_big_endian)
        cache["hex_big_endian"].append(hex_big_endian)

if __name__ == '__main__':
    # Example usage
    text = "Hello World. My name is John Doe. I am a software engineer"
    sha1 = SHA1(text)
    sha1.generate_hash()
    print("Hash (Hex):", sha1.hash_hex)
    import hashlib
    sha1_hash = hashlib.sha1(text.encode("utf-8")).hexdigest()
    print("Hash (Hex) hashlib:", sha1_hash)
