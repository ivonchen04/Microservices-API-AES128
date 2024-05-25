from flask import Flask, request, jsonify
from Crypto.Cipher import AES
import base64

app = Flask(__name__)
key = b'This is a key123'  # Kunci 16 byte

def decrypt_message(encrypted_message):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = encrypted_message[:16]
    ciphertext = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message.decode('utf-8')

@app.route('/secure_message', methods=['POST'])
def secure_message():
    data = request.json
    encrypted_message = base64.b64decode(data['message'])
    decrypted_message = decrypt_message(encrypted_message)
    print(f"Received encrypted message: {decrypted_message}")
    return jsonify({"response": "Encrypted message received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
