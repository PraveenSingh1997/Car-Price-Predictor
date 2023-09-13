from flask import Flask , render_template 

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


if __name__ == "Hello World":
    app.run(debug = True)