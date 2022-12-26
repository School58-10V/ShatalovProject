import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/quotes", methods=["GET"])
def get_quotes():
    with open("base.json", encoding="utf-8-sig") as f:
        text_data = f.read()
        data = json.loads(text_data)
        return jsonify(data)


@app.route("/quotes/<int:id>", methods=["GET"])
def get_quotes_by_id(id):
    with open("base.json", encoding="utf-8-sig") as f:
        text_data = f.read()
        data = json.loads(text_data)
        quote = data["quotes"][str(id)]
        return jsonify(quote)



@app.route("/quotes", methods=["POST"])
def create_quotes():
    quote = request.get_json()["quote"]
    with open("base.json", encoding="utf-8") as f:
        data = json.load(f)

    current_id = str(len(data["quotes"].keys()) + 1)
    data["quotes"][current_id] = quote
    with open("base.json", 'w', encoding='utf-8') as f:
        json.dump(data, f)

    return current_id


if __name__ == "__main__":
    app.run()