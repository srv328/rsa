# Educational RSA Implementation in Python

This is a basic implementation of the RSA algorithm in Python for educational purposes. It demonstrates the fundamental steps of RSA:

- Key Generation: Generating public and private keys using prime numbers.
- Encryption: Encrypting a message using the recipient's public key.
- Decryption: Decrypting a ciphertext using the recipient's private key.

## Important Note:

**This implementation is NOT suitable for real-world cryptographic applications.** It is designed for learning and understanding the RSA algorithm only. It has several vulnerabilities, including potential weaknesses in prime generation and lack of secure padding, making it insecure for practical use. 

## How to Use:

1. **Run the script:**
   ```bash
   python rsa.py
   ```
2. **Input:**
   - You will be prompted to enter the desired key size in bits.
   - Enter the plaintext message you want to encrypt.
3. **Output:**
   - The script will display the generated public and private keys.
   - It will then show the encrypted ciphertext and the decrypted plaintext.

## Files:

- **rsa.py:**  The Python script containing the RSA implementation.

## Limitations:

- **Security:** This is an insecure implementation for educational purposes only. 
- **Prime Generation:** Prime generation may not be cryptographically secure.
- **Padding:** No padding scheme is used, making it vulnerable to attacks.

## Learning Resources:

- [RSA (cryptosystem) - Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Cryptography library for Python](https://cryptography.io/en/latest/) (for secure implementations)

## Disclaimer:

Use this code responsibly. The authors are not responsible for any consequences arising from its use in insecure environments. 
