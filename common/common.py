from bitarray import bitarray
from bitarray.util import ba2int

def hex_to_bin(hex_string, version=32) -> bitarray:
    hex_string = hex_string.replace(" ", "")
    return bitarray(bin(int(hex_string, 16))[2:].zfill(version))

def bin_to_hex(bin_array, version=32) -> str:
    hex_string = format(ba2int(bin_array), 'X').zfill(version // 4)
    return ' '.join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))

def str_to_bin(message: str) -> bitarray:
    binary_message = bitarray()
    binary_message.frombytes(message.encode("ISO-8859-1"))

    return binary_message

def add_padding_bytes(binary_message: bitarray) -> list[bitarray]:
    n = len(binary_message)
    # add padding
    binary_message += bitarray("1")
    k = len(binary_message) % 512
    if k <= 448:
        binary_message += bitarray("0" * (448 - k))
    elif k > 448:
        binary_message += bitarray("0" * (512 - k + 448))
    binary_message += hex_to_bin(n.to_bytes(8, byteorder='little').hex(), 64)

    return [binary_message[i:i+512] for i in range(0, len(binary_message), 512)]

def block_512_bit_to_str(blocks: bitarray) -> str:
    binary_string = bitarray()
    for block in blocks:
        binary_string += block
    return binary_string.tobytes().decode("ISO-8859-1")

def block_to_little_endian(block: bitarray) -> bitarray:
    result = bitarray()
    for i in range(0, len(block), 32):
        block_32_bit = block[i:i+32]
        bytes = [block_32_bit[j:j+8] for j in range(0, len(block_32_bit), 8)]
        bytes.reverse()
        for byte in bytes:
            result += byte
    return result



if __name__ == '__main__':
    # message 215 bits
    messages = "Hello world! This is a test message."
    binary_message = str_to_bin(messages)
    res = str_to_blocks_512_bit(binary_message)
    #print(bin_to_hex(res[0]))

    print(bin_to_hex(block_to_little_endian(hex_to_bin("67 45 23 01"))))