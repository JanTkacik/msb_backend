#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/hackaton/backend', methods=['GET'])
def predictive_maintanance_zeroloss():
    return jsonify({'response': 1})


if __name__ == '__main__':
    print(os.environ['FLASK_APP'])
    app.run(debug=True)
