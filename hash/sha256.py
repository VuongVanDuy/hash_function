import math
from bitarray import bitarray
from bitarray.util import ba2int, int2ba
from common.common import (bin_to_hex, hex_to_bin, str_to_bin, add_padding_bytes)

K_SHA256 = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]


class SHA256:
    def __init__(self, text: str = None):
        self.text = text
        self.blocks = []
        self.hash_bin = ""
        self.hash_hex = ""
        self.cache = {}
        # Các hàm logic của SHA256
        self.__f_functions = [
            lambda x, y, z: (x & y) ^ (x & z) ^ (y & z),  # Maj
            lambda x, y, z: (x & y) ^ (~x & z),  # Ch
        ]
        self.__shift_constants = [
            [2, 13, 22],   # Dùng cho Sigma0
            [6, 11, 25],   # Dùng cho Sigma1
            [7, 18, 3],    # Dùng cho sigma0
            [17, 19, 10]   # Dùng cho sigma1
        ]
        self.__K = self.generate_K()

    def generate_K(self):
        K = []
        for i in range(64):
            K.append(int2ba(K_SHA256[i], length=32))
        return K

    def add_operator(self, operandA: bitarray, operandB: bitarray) -> bitarray:
        intA = ba2int(operandA)
        intB = ba2int(operandB)
        result = (intA + intB) & 0xFFFFFFFF
        return int2ba(result, length=32)

    def rotate_right(self, x: bitarray, n: int) -> bitarray:
        # Dịch vòng phải x qua n bit và đảm bảo kết quả luôn 32-bit
        return ((x >> n) | (x << (32 - n))) & bitarray("1" * 32)

    def shift_right(self, x: bitarray, n: int) -> bitarray:
        # Dịch phải x qua n bit mà không cần vòng
        return x >> n

    def SIGMA_0(self, x: bitarray) -> bitarray:
        return self.rotate_right(x, self.__shift_constants[0][0]) ^ \
               self.rotate_right(x, self.__shift_constants[0][1]) ^ \
               self.rotate_right(x, self.__shift_constants[0][2])

    def SIGMA_1(self, x: bitarray) -> bitarray:
        return self.rotate_right(x, self.__shift_constants[1][0]) ^ \
               self.rotate_right(x, self.__shift_constants[1][1]) ^ \
               self.rotate_right(x, self.__shift_constants[1][2])

    def sigma_0(self, x: bitarray) -> bitarray:
        return self.rotate_right(x, self.__shift_constants[2][0]) ^ \
               self.rotate_right(x, self.__shift_constants[2][1]) ^ \
               self.shift_right(x, self.__shift_constants[2][2])

    def sigma_1(self, x: bitarray) -> bitarray:
        return self.rotate_right(x, self.__shift_constants[3][0]) ^ \
               self.rotate_right(x, self.__shift_constants[3][1]) ^ \
               self.shift_right(x, self.__shift_constants[3][2])

    def generate_words(self, block: bitarray) -> list[bitarray]:
        words = []
        for i in range(16):
            word_i = block[i * 32:(i + 1) * 32]
            words.append(word_i)
        for i in range(16, 64):
            res_sigma_0 = self.sigma_0(words[i - 15])
            res_sigma_1 = self.sigma_1(words[i - 2])
            tmp = self.add_operator(words[i - 16], res_sigma_0)
            tmp = self.add_operator(tmp, words[i - 7])
            tmp = self.add_operator(tmp, res_sigma_1)
            words.append(tmp)
        return words

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

        # Step 3: Initialize the SHA256 state variables
        H = [
            hex_to_bin("6a09e667", 32),
            hex_to_bin("bb67ae85", 32),
            hex_to_bin("3c6ef372", 32),
            hex_to_bin("a54ff53a", 32),
            hex_to_bin("510e527f", 32),
            hex_to_bin("9b05688c", 32),
            hex_to_bin("1f83d9ab", 32),
            hex_to_bin("5be0cd19", 32)
        ]
        self.cache["initialize_SHA_buffer"] = {
            "int_big_endian": [],
            "hex_big_endian": []
        }
        self.addEndOfBlockToCache(self.cache["initialize_SHA_buffer"], H)

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
            words = self.generate_words(block)
            self.addWordsToBlockCache(self.cache[f"block_{k}"]["words_of_block"], words)

            # Step 5: Initialize the working variables for this block
            a, b, c, d, e, f, g, h = H

            # Step 6: Compression function main loop
            for i in range(64):
                interm_res = []
                S1 = self.SIGMA_1(e)
                ch = self.__f_functions[1](e, f, g)

                temp1 = self.add_operator(h, S1)
                interm_res.append(temp1)
                temp1 = self.add_operator(temp1, ch)
                interm_res.append(temp1)
                temp1 = self.add_operator(temp1, self.__K[i])
                interm_res.append(temp1)
                temp1 = self.add_operator(temp1, words[i])
                interm_res.append(temp1)
                S0 = self.SIGMA_0(a)
                maj = self.__f_functions[0](a, b, c)
                # tính T2 = Σ₀(a) + Maj(a,b,c)
                temp2 = self.add_operator(S0, maj)
                interm_res.append(temp2)

                self.addIntermediateResultsToCache(self.cache[f"block_{k}"]["intermediate_results"],
                                                   step=i,
                                                   results=interm_res)

                # Cập nhật các biến làm việc theo đúng định nghĩa:
                h = g
                g = f
                f = e
                e = self.add_operator(d, temp1)
                d = c
                c = b
                b = a
                a = self.add_operator(temp1, temp2)

                self.addNewStateToCache(self.cache[f"block_{k}"]["buffers_state"],
                                        states=[a, b, c, d, e, f, g, h,
                                                S1, S0, maj, ch, temp1, temp2, self.__K[i]])

            # Step 7: Add the compressed chunk to the current hash value
            H[0] = self.add_operator(H[0], a)
            H[1] = self.add_operator(H[1], b)
            H[2] = self.add_operator(H[2], c)
            H[3] = self.add_operator(H[3], d)
            H[4] = self.add_operator(H[4], e)
            H[5] = self.add_operator(H[5], f)
            H[6] = self.add_operator(H[6], g)
            H[7] = self.add_operator(H[7], h)
            self.addEndOfBlockToCache(self.cache[f"block_{k}"]["end_of_block"], [H[0], H[1], H[2], H[3], H[4], H[5], H[6], H[7]])
            k += 1

        # Step 8: Produce the final hash value
        self.hash_bin = ''.join([h.to01() for h in H])
        self.hash_hex = ' '.join([bin_to_hex(h) for h in H])

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
    sha256 = SHA256(text)
    sha256.generate_hash()
    print("Hash (Hex):", sha256.hash_hex)
    import hashlib
    sha1_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("Hash (Hex) hashlib:", sha1_hash)
