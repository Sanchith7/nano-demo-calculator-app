from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return jsonify({"message": "Hello world!"}), 200

@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify({"error": "Both 'first' and 'second' must be provided."}), 400

   


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
