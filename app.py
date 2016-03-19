from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello():
	return "Hello World!"

if __name__ == '__main__':
	app.run("0.0.0.0")
