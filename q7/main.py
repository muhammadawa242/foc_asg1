import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_aes_gcm(key, plaintext):
    # Generate a random 96-bit IV (12 bytes)
    iv = os.urandom(12)
    
    # Create AES GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Perform encryption
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    tag = encryptor.tag
    
    return iv, ciphertext, tag

def decrypt_aes_gcm(key, iv, ciphertext, tag):
    # Create AES GCM cipher for decryption
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()

    # Perform decryption
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_text

def modify_bit(data, bit_position):
    # Convert byte array to bit array
    byte_index = bit_position // 8
    bit_index = bit_position % 8
    modified_data = bytearray(data)
    
    # Flip the specified bit
    modified_data[byte_index] ^= (1 << bit_index)
    
    return modified_data

def main():
    # Key should be 16 bytes (128 bits)
    key = os.urandom(16)
    
    # Sample plaintext
    plaintext = b'This is a test message for AES-128-GCM encryption.'

    # Encrypt the plaintext
    iv, ciphertext, tag = encrypt_aes_gcm(key, plaintext)

    print(f'Original Ciphertext: {ciphertext.hex()}')
    print(f'Tag: {tag.hex()}')

    # Modify a single bit in the ciphertext
    modified_ciphertext = modify_bit(ciphertext, 5)  # Modify the 6th bit
    print(f'Modified Ciphertext: {modified_ciphertext.hex()}')

    # Attempt to decrypt the modified ciphertext
    try:
        decrypted_text = decrypt_aes_gcm(key, iv, modified_ciphertext, tag)
        print(f'Decrypted Text (modified CT): {decrypted_text.decode()}')
    except Exception as e:
        print(f'Decryption failed (modified CT): {e}')

    # Modify a single bit in the tag
    modified_tag = modify_bit(tag, 3)  # Modify the 4th bit
    print(f'Modified Tag: {modified_tag.hex()}')

    # Attempt to decrypt with the modified tag
    try:
        decrypted_text = decrypt_aes_gcm(key, iv, ciphertext, modified_tag)
        print(f'Decrypted Text (modified Tag): {decrypted_text.decode()}')
    except Exception as e:
        print(f'Decryption failed (modified Tag): {e}')

if __name__ == "__main__":
    main()
