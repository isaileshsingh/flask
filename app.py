from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world!"


if "__name" == "__main__":
    app.run(debug=True)
