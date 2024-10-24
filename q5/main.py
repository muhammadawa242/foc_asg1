from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encrypt_aes_ecb(key, plaintext):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(plaintext) + encryptor.finalize()

def pad(plaintext):
    padding_length = 16 - len(plaintext) % 16
    return plaintext + bytes([padding_length] * padding_length)

if __name__ == "__main__":
    key = os.urandom(16)  # Generate a random 128-bit key

    # Example plaintext with identical blocks
    plaintext1 = b"This is block 1.  "  # 16 bytes
    plaintext2 = b"This is block 1.  "  # Same as above

    ciphertext1 = encrypt_aes_ecb(key, pad(plaintext1))
    ciphertext2 = encrypt_aes_ecb(key, pad(plaintext2))

    print(f'Ciphertext 1: {ciphertext1.hex()}')
    print(f'Ciphertext 2: {ciphertext2.hex()}')
