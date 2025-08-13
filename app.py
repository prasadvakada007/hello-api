from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello World")

if __name__ == "__main__":
    # 0.0.0.0 is important so Docker can expose it
    app.run(host="0.0.0.0", port=5000)
