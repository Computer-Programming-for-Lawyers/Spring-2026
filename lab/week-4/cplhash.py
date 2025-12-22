### Name: Jonathan Frankle
### Filename: hash.py
### Created 1/20/17  Updated: 1/20/17
### Description: A library that wraps a hash function.
###     * If executed from the terminal, it takes a password as a command-line argument
###       and prints the hash of that password.
###     * If imported with 'import hash', it provides the function hash.md5_hash() which
###       takes a string password as an argument and returns a string hash.
### Dependencies: hashlib

import hashlib
import sys

# Computes the hash of a string <s>. Returns a string representing the hash.
def md5_hash(s):
    md5Obj = hashlib.md5()
    md5Obj.update(s.encode('utf-8'))
    return md5Obj.hexdigest()
    
def short_hash(s):
    return md5_hash(s)[:3]
    
# If this script is run directly, it hashes its command-line argument.
if __name__ == '__main__':
    # Ensure there are enough command-line arguments.
    if len(sys.argv) < 2:
        print('Provide a password to be hashed as a command-line argument.')
     
    # Otherwise, hash the password and print it.
    else:
        password = sys.argv[1]
        print(md5_hash(password))
