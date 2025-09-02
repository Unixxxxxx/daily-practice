from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple Hello World API
    ---
    responses:
      200:
        description: Returns a greeting message
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify({"message": "Hello, World!"})


@app.route('/add', methods=['POST'])
def add_numbers():
    """
    Add two numbers
    ---
    parameters:
      - name: num1
        in: query
        type: integer
        required: true
      - name: num2
        in: query
        type: integer
        required: true
    responses:
      200:
        description: The sum of two numbers
        examples:
          application/json: {"sum": 5}
    """
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    return jsonify({"sum": num1 + num2})


if __name__ == "__main__":
    app.run(debug=True)
# http://127.0.0.1:5000/apidocs/ 
#
