from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    print(f"Received message: {data['message']}")
    return jsonify({"response": "Message received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
