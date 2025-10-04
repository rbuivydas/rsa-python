# RSA Encryption and Decryption Tool using Python

## What is RSA?

RSA is an encryption method for securely communicating with individuals using asymmetric encryption where two different keys are used to cipher and decipher text, a public key and a private key. A public encryption key is used to generate ciphertext which is channelled through a communication channel to the desired individual. For the individual on the other end to be able to read the ciphertext, a private decryption key is required which can decrypt the ciphertext.

## Variables Used for Python RSA Code

| Variable | Definition |
| -------- | ---------- |
| P        | Large Prime Number 1 |
| Q        | Large Prime Number 2 |
| n        | P x Q (public modulus) |
| phi(n)   | (p-1)(q-1) Euler's Totient |
| e        | Public Exponent, (1 < e < phi(n)) && GCD(e, phi(n)) = 1) |
| d        | Private Exponent, ed = 1 mod phi(n) or d = $e^-1$ mod(phi(n)) |
| (e, n)   | Public Key |
| (d, n)   | Private Key |

All of these variables are required for the RSA algorithm to function properly and calculate public, private keys accordingly.

## Encryption and Decryption Formula

Encryption: $M^e$ mod q

Decryption: $C^d$ mod q

With encryption, the formula will convert the plaintext to ciphertext using the public key. As for decryption, the ciphertext will be converted to plaintext using the private key.

# [Python Code](https://github.com/rbuivydas/rsa-python/blob/main/code.py)
