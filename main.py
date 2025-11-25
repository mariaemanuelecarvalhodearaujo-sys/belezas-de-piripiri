import os

from flask import Flask, render_template, send_file


app = Flask(__name__,static_folder='src/static', template_folder='src/templates')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('src/static/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)
