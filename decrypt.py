import sys
import os
from Cryptodome.Cipher import AES

def decrypt_file(path):
    with open(path, "rb") as file_in:
        ciphertext = file_in.read()

    key = b'this is a 16 key'

    iv = ciphertext[:AES.block_size]
    actual_ciphertext = ciphertext[AES.block_size:]

    mycipher = AES.new(key, AES.MODE_CFB, iv)
    plaintext = mycipher.decrypt(actual_ciphertext)

    # Get decrypt.py folder path
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Extract filename without '.bin'
    filename = os.path.basename(path)[:-4]

    # Build new output path inside decrypt.py folder
    original_path = os.path.join(script_dir, filename)

    with open(original_path, "wb") as file_out:
        file_out.write(plaintext)

    print(f"Decrypted: {original_path}")

def decrypt_dir(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".bin"):
                file_path = os.path.join(root, file)
                print(file_path + " is decrypting.")
                decrypt_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decrypt.py <path_to_file_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    if os.path.isdir(path) and os.path.exists(path):
        decrypt_dir(path)
    elif os.path.isfile(path) and os.path.exists(path):
        decrypt_file(path)
    else:
        print("It's a special file (socket, FIFO, or device file)")
