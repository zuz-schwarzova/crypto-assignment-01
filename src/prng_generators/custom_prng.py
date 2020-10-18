from Crypto.Cipher import AES


'''
Helper exclusive-or function for byte parameters.
Source: https://nitratine.net/blog/post/xor-python-byte-strings/

:param param1: bytes parameter
:param param2: bytes parameter
:returns: byte value of XOR-ed parameters
'''
def byte_xor(param1, param2):
    return bytes([_x ^ _y for _x, _y in zip(param1, param2)])


'''
Custom implementation of 128bit ANSI X9.31 pseudorandom number generator.

AES implementation used from PyCryptodome Python package:
https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

:param byte_size: desired size of generated data (in bytes)
:returns: bytearray of pseudorandom data
'''
def ansiX931prng(byte_size):
    block_size = 16
    # repetitions of uco for initial seed, for cipher block size 16bytes (128bits)
    ucoList = [4, 3, 3, 5, 2, 9, 4, 3, 3, 5, 2, 9, 4, 3, 3, 5]
    # V is initial 128bit seed, as hexadecimal characters
    V = bytearray(ucoList)
    # K is 128bit encryption key, as hexadecimal characters
    K = bytearray(reversed(ucoList))
    # dtv is Date/Time vector
    dtv = 0
    # initializing of empty result
    result = bytearray()
    # creating a new AES cipher, with encryption under key K
    edeK = AES.new(K, AES.MODE_ECB)

    # loop with ANSI X9.31 algorithm for getting blocks of pseudorandom data
    # keeps extending result until desired size
    while len(result) < byte_size:
        # calculating intermediate value I
        # Date/Time vector (as hexadecimal), encrypted with AES cipher edeK
        I = edeK.encrypt(dtv.to_bytes(block_size, 'big'))
        # creating block of pseudorandom data R
        # XOR of intermediate value I and initial seed V, encrypted with AES cipher edeK
        R = edeK.encrypt(byte_xor(I, V))
        # creating a new seed V
        # XOR of pseudorandom data R and intermediate value I, encrypted with AES cipher edeK
        V = edeK.encrypt(byte_xor(R, I))
        # extending result by pseudorandom data R, until it reaches desired byte size
        result.extend(R[:byte_size - len(result)])
        # updating Date/Time vector for next iteration
        dtv = dtv + 1
    return result


