from helper.sudoku_table import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def game():
	return "test"

if __name__ == "__main__":
	app.run()