from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory('src/templates', 'index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
