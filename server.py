from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET']) 
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()

    if 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    num1 = data['first']
    num2 = data['second']
    result = num1 + num2

    return jsonify({'result': result})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()

    if 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    num1 = data['first']
    num2 = data['second']
    result = num1 - num2

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
