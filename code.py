# RSA Encryption & Decryption Algorithm
# Author: github.com/rbuivydas
# Date: 01/2025

import random
import time
from sympy import mod_inverse
from progress.bar import Bar

def RSA_setup(p, q):
    if not (isPrime(p) and isPrime(q)):
        return "Both values must be prime"
    elif p == q:
        return "Both values must not be the same!"
    
    # A part of the RSA public key {(e,n)}
    N = p * q
    
    # A part of the RSA private key {(d,n)} // Euler's Totient
    R = (p-1) * (q-1)
    
    # Create a value for e to be coprime with phi(R)
    e = random.randrange(1, R)
    
    # Check if e is coprime with phi(R) using gcd function
    g = gcd(e, R)
    while g != 1:
        e = random.randrange(1, R)
        g = gcd(e, R)
    
    # Modular inverse to find 'd' part of private key, using extended euclidean algorithm (ex+Ry = gcd(e, R))
    d = mod_inverse(e, R)
    
    # Incorrect dummy key generated for an IDS to be in place
    n1 = random.randrange(0, 1000)
    n2 = random.randrange(0, 1000)
    
    # Returns public key {(e,n)} and private key {(d,n)}
    return (e, N),(d, N),(n1, n2)

# Encryption function
def RSA_enc(plain, pk):
    # Key is unpacked into its components
    e, n = pk
    cipher = [pow(ord(char), e, n) for char in plain] # Encryption on each character of plaintext messsage
    
    return cipher

# Decryption function
def RSA_dec(cipher, pk):
    # Key is unpacked into its components
    d, n = pk
    plain = ''.join(chr(pow(char, d, n)) for char in cipher) # Retrieves plaintext value by applying modular exponentiation
    
    return plain

# Function for calculating the GCD of two numbers        
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

# To check if p and q are prime numbers
def isPrime(n):
    n = abs(int(n)) # Ensure that n is a positive number
    
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
        return True

# Progress bar for user interaction   
def progress_bar(cycle, x, txt):
    with Bar(f"{txt}") as bar:
        for i in range(cycle):
            time.sleep(x)
            bar.next()

print("###########################################")
print("#       RSA Encryptor/Decryptor Tool      #")
print("#       Author: github.com/rbuivydas      #")
print("###########################################" + "\n")

if __name__ == "__main__":
    # Loop until user decides to terminate program
    while True:
        
        main_menu = input("1) Encryption" + "\n" + 
                          "2) Decryption" + "\n" + 
                          "3) Exit"       + "\n" + 
                        "---------------" + "\n" + 
                          "Selection: ")
        
        if main_menu == "1":
            try:
                while True:
                    a = input("Enter a prime number (e.g. 23, 29, 37, 59): ")
                    b = input(f"Enter a prime number (not {a}): ")
                
                    if not a:
                        print("Please enter a prime number!")
                        continue
                    elif not b:
                        print("Please enter a prime number!")
                        continue
                    else:
                        break
                
                public, private, dummy_key = RSA_setup(int(a), int(b)) # Assign public and private keys to a,b
                
                print("Public Key:", public)
                
                with open("privatekey.txt", "w") as f:
                    f.write(str(private))
                    
            except ValueError: # Incorrect value entered returns an error and prompts re-entry of value
                print(RSA_setup(a, b), "\n")
                continue
            
            msg = input("Enter a filename to encrypt (ignore .txt): ")
            
            try:
                # Open the file specified by the user with read permissions
                with open(f"{msg}.txt", "r") as f:
                    # Encrypted message using public key and file contents
                    enc_msg = RSA_enc(f.read(), public)
                
                # New text file created with encrypted message
                with open(f"encrypted_{msg}.zxzx", "w") as f:
                    f.write(" ".join(map(str, enc_msg)))  # Write to the file as space-separated values
                   
                progress_bar(100, 0.03, "Encrypting...")
                
                # Shows the encrypted message to the user
                print("Encrypted message: ", ''.join(map(lambda x: str(x), enc_msg)))
                print(f"File name: encrypted_{msg}.zxzx")
            except FileNotFoundError: # If the file does not exist it will produce an error
                print(f"File {msg}.zxzx not found!")
            continue
            
        elif main_menu == "2":
            
            msg = input("Enter a filename to decrypt (ignore .zxzx): ")
            
            print("-----------------------------------------")
            print("---   Private key format is (d, n)    ---")
            print("-----------------------------------------", "\n")
            
            d = int(input("Enter d: "))
            n = int(input("Enter n: "))
            
            key_choice = d, n
                
            try:
                with open(f"{msg}.zxzx", "r") as f:
                    # Read encrypted message from the file
                    enc_msg_s = f.read().strip()
                    enc_msg = list(map(int, enc_msg_s.split()))  # Considering space-separated values
                    
                    print("Encrypted message: ", ''.join(map(lambda x: str(x), enc_msg)))
                    print("Decrypting with private key: ", key_choice)
                    
                    # Decrypt message with the private key
                    dec_msg = RSA_dec(enc_msg, key_choice)
                    
                    progress_bar(100, 0.03, "Decrypting...")
                    
                    print("Decrypted message:", dec_msg)
            except FileNotFoundError:
                print(f"File {msg} not found!")
            continue
            
        else:
            break

    print("###########################################################")
    print("# Thank you for using RSA encryption/decryption. Goodbye! #")
    print("###########################################################")
