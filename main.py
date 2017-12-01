#!flask/bin/python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/msb/getscore', methods=['POST'])
def predictive_maintanance_zeroloss():
    try:
        indata = json.loads(request.data.decode("utf-8"))
        return jsonify(
            {
                "results":
                [
                    {
                        "Score": 43242,
                        "Product": {
                            "Name": "Clovek",
                            "Price": 321312
                        },
                        "ProCons":
                        [
                            {
                                "Type": "Pro",
                                "Reason": "Vacsi penis o 3cm"
                            },
                            {
                                "Type": "Cons",
                                "Reason": "Horsi ksicht"
                            }
                        ]
                    }
                ]
            }
        )
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    print(os.environ['FLASK_APP'])
    app.run(debug=True)
