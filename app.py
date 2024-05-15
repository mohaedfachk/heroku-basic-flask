iffrom flask import Flask
app = Flask(__name__)
@app.route("/")
def f():
	return '<h1>Hello</h1>'



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
