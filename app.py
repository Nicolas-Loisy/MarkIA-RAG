from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemple d'endpoint
@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, Firebase!'})

# Endpoint avec un paramètre
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({'you_sent': data})

if __name__ == '__main__':
    app.run(debug=True)
