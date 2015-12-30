from helper.puzzle_creator import create_puzzle
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def game():
	p = create_puzzle(5)
	# return render_template('game.html', puzzle = [[1,2],[3,4]])
	return render_template('game.html.py', puzzle = p)

if __name__ == "__main__":
	app.run()