import json

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from solution import solve_sudoku

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/solution', methods=['GET'])
def solution():
	grid = json.loads(request.args['data'])
	if(solve_sudoku(grid)):
		return jsonify({"message":"Success", "data":grid})
	else:
		return jsonify({"message":"Failed!!!, No solution exists", "data":grid})

if __name__ == "__main__":
	app.run(debug=True)
