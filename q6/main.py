import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_aes_cbc(key, plaintext):
    iv = os.urandom(16)  # 16 bytes IV for AES
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad plaintext to be multiple of block size
    padding_length = 16 - len(plaintext) % 16
    plaintext += bytes([padding_length] * padding_length)
    
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return iv, ciphertext

def decrypt_aes_cbc(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    padding_length = decrypted_padded[-1]
    return decrypted_padded[:-padding_length]

def encrypt_aes_ctr(key, plaintext):
    iv = os.urandom(16)  # 16 bytes nonce/IV for AES
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return iv, ciphertext

def decrypt_aes_ctr(key, iv, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def modify_bit(data, bit_position):
    byte_index = bit_position // 8
    bit_index = bit_position % 8
    modified_data = bytearray(data)
    modified_data[byte_index] ^= (1 << bit_index)
    return modified_data


def main():
    key = os.urandom(16)  # 128-bit key
    plaintext = b'This is a test message for AES-128.'

    # AES-128-CBC
    iv_cbc, ciphertext_cbc = encrypt_aes_cbc(key, plaintext)
    print(f'AES-CBC Ciphertext: {ciphertext_cbc.hex()}')
    
    # Modify a bit in the ciphertext
    modified_ciphertext_cbc = modify_bit(ciphertext_cbc, 10)  # Modify the 11th bit
    print(f'Modified AES-CBC Ciphertext: {modified_ciphertext_cbc.hex()}')

    # Decrypt modified ciphertext
    try:
        decrypted_cbc = decrypt_aes_cbc(key, iv_cbc, modified_ciphertext_cbc)
        print(f'Decrypted AES-CBC (modified CT): {decrypted_cbc.decode()}')
    except Exception as e:
        print(f'AES-CBC Decryption failed (modified CT): {e}')

    # AES-128-CTR
    iv_ctr, ciphertext_ctr = encrypt_aes_ctr(key, plaintext)
    print(f'AES-CTR Ciphertext: {ciphertext_ctr.hex()}')

    # Modify a bit in the ciphertext
    modified_ciphertext_ctr = modify_bit(ciphertext_ctr, 10)  # Modify the 11th bit
    print(f'Modified AES-CTR Ciphertext: {modified_ciphertext_ctr.hex()}')

    # Decrypt modified ciphertext
    decrypted_ctr = decrypt_aes_ctr(key, iv_ctr, modified_ciphertext_ctr)
    print(f'Decrypted AES-CTR (modified CT): {decrypted_ctr.decode()}')


if __name__ == "__main__":
    main()
