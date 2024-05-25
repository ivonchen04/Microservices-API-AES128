import requests
from Crypto.Cipher import AES
import base64

key = b'This is a key123'  # Kunci 16 byte

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

message = "Hello, Secure Server!"
encrypted_message = encrypt_message(message)
payload = {"message": encrypted_message}

response = requests.post("http://127.0.0.1:5001/secure_message", json=payload)
print(response.json())
