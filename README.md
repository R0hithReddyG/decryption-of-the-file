---

# AES File and Directory Decryption Tool

This Python script provides a utility for decrypting files or entire directories encrypted using AES in Cipher Feedback (CFB) mode. It is intended to be used in conjunction with a compatible AES encryption script that prepends the Initialization Vector (IV) to the encrypted data.

---

## Features

* **File Decryption**
  Decrypts a single `.bin` file produced by the encryption script.

* **Directory Decryption**
  Recursively decrypts all `.bin` files in a directory and its subdirectories.

* **AES-CFB Mode**
  Uses AES Cipher Feedback (CFB) mode to securely handle encrypted files without padding.

* **Automatic Output Management**
  Restores decrypted files to the directory where `decrypt.py` is located, with the `.bin` extension removed.

---

## Prerequisites

* **Python 3.6 or higher**
* **pycryptodomex library**

To install `pycryptodomex`, run:

```
pip install pycryptodomex
```

---

## Usage

Run the script from the command line:

```
python decrypt.py <path_to_file_or_directory>
```

### Parameters

* `<path_to_file_or_directory>` :
  The file or directory containing encrypted `.bin` files to be decrypted.

---

## Examples

**Decrypt a single file**

```
python decrypt.py encrypted_document.txt.bin
```

**Decrypt all encrypted files in a directory**

```
python decrypt.py /path/to/encrypted_folder
```

---

## How It Works

1. The script reads the encrypted file as binary data.
2. It extracts the Initialization Vector (IV) from the first 16 bytes of the file.
3. The remainder is treated as the ciphertext.
4. The AES cipher is initialized with the specified key and IV.
5. The ciphertext is decrypted.
6. The plaintext is saved in the same directory as `decrypt.py`, using the original filename (without `.bin`).

---

## Important Notes

* **Key Management**
  The script uses a hard-coded key (`this is a 16 key`). Ensure this matches the key used during encryption. For secure applications, replace this key with a securely managed secret key.

* **Output Location**
  All decrypted files are saved to the directory where `decrypt.py` is located. Ensure you have the necessary permissions to write to this location.

* **File Types**
  The script processes files ending with `.bin` only. Other files are ignored.

---

## License

This project is made available under the MIT License. You are free to use, modify, and distribute the code with appropriate credit.

---

## Contributions

Contributions and improvements are welcome. Please open an issue or submit a pull request to contribute to this tool.

---
