import random

'''
Implementation of pseudo-random number generator with seed, using Python native functions for random

:param byte_size: desired size of generated data (in bytes)
:returns: pseudorandom byte data of desired size
'''
def nativeprng(byte_size):
    # repetitions of uco for initial seed, for cipher block size 16bytes (128bits)
    ucoList = [4, 3, 3, 5, 2, 9, 4, 3, 3, 5, 2, 9, 4, 3, 3, 5]
    # seed, as hexadecimal characters
    seed = bytearray(ucoList)
    #create an instance of Random with given seed
    random.seed(seed)
    #get random bits
    randbits = random.getrandbits(10**9)
    #convert random bits to desired byte size
    result = randbits.to_bytes(byte_size, 'big')
    return result
