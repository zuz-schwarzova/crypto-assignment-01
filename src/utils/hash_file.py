import hashlib

'''
Algorithm for finding a SHA256 hash string of a file.
Source: https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html

:param filename: name/path to the file
:returns: string hash of a given file
'''
def sha256sum(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as file:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
