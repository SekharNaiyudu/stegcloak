#!/usr/bin/env python3

import argparse
from stegano import lsb
from cryptography.fernet import Fernet
import base64
import os
import sys

def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(password.ljust(32)[:32].encode())

def encrypt_message(message: str, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(encrypted: str, password: str) -> str:
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted.encode()).decode()

def encode_image(input_img, output_img, message, password=None):
    if password:
        message = encrypt_message(message, password)
    secret_img = lsb.hide(input_img, message)
    secret_img.save(output_img)
    print(f"[+] Message successfully hidden in {output_img}")

def decode_image(image, password=None):
    hidden_message = lsb.reveal(image)
    if not hidden_message:
        print("[-] No hidden message found.")
        return
    if password:
        try:
            hidden_message = decrypt_message(hidden_message, password)
        except Exception as e:
            print("[-] Decryption failed. Wrong password?")
            return
    print(f"[+] Hidden message: {hidden_message}")

def banner():
    print(r"""
  _____ _                   _                      
 / ____| |                 | |                     
| (___ | |_ ___  _ __   ___| |_ ___  ___ ___  _ __ 
 \___ \| __/ _ \| '_ \ / _ \ __/ _ \/ __/ _ \| '__|
 ____) | || (_) | | | |  __/ ||  __/ (_| (_) | |   
|_____/ \__\___/|_| |_|\___|\__\___|\___\___/|_|   

           StegCloak - LSB Stego + Crypto
""")

def main():
    banner()
    parser = argparse.ArgumentParser(description="Steganography Tool for Encoding/Decoding Messages in Images")
    parser.add_argument('-m', '--mode', choices=['encode', 'decode'], required=True, help="Mode: encode or decode")
    parser.add_argument('-i', '--input', required=True, help="Input image path")
    parser.add_argument('-o', '--output', help="Output image path (required for encoding)")
    parser.add_argument('-s', '--secret', help="Secret message (for encoding)")
    parser.add_argument('-p', '--password', help="Optional password to encrypt/decrypt message")

    args = parser.parse_args()

    if args.mode == 'encode':
        if not args.secret or not args.output:
            print("[-] Encoding requires --secret and --output")
            sys.exit(1)
        encode_image(args.input, args.output, args.secret, args.password)
    elif args.mode == 'decode':
        decode_image(args.input, args.password)

if __name__ == '__main__':
    main()
