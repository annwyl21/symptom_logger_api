from flask import Flask, request, jsonify
from Summarize import Summarize

app = Flask(__name__)

@app.route('/slapi/summarize', methods=['GET', 'POST'])
def summarize():
	if request.method == 'POST':
		data = request.json
		data = data['data']
	
		summary = Summarize.create_summary(data)

		return jsonify(summary)
	
	else:
		return jsonify({"error": "No data to summarize"})

if __name__ == '__main__':
	app.run(debug=True)
	#app.run()