from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/getstatus')
def getstatus():
    return 'The service should be working.'

@app.route('/main')
def main():
	page = request.args.get('page', default = 1, type = int)
	filter = request.args.get('filter', default = '*', type = str)
	return f"Test{page, filter}"


if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=80
	)