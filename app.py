from flask import Flask, request, jsonify
from Summarize import Summarize
from summarize_ai import summarize_with_ai
import re

app = Flask(__name__)

# AI_key = False
AI_key = True

@app.route('/slapi/summarize', methods=['GET', 'POST'])
def summarize():
	if request.method == 'POST':
		data = request.json
	
		if AI_key == True:
			summary = summarize_with_ai(data).choices[0].text
			
			# extract info from result
			# Define the regex patterns for Summary, Status, and Time Period
			patterns = {
				'Summary': r'Summary: (.*?)(?= Status:|$)',
				'Status': r'Status: (.*?)(?= Time Period:|$)',
				'Period': r'Period: (.*)'
			}
			
			extracted_info = {}
			for key, pattern in patterns.items():
				match = re.search(pattern, summary, re.DOTALL)
				if match:
					extracted_info[key] = match.group(1).strip()

			summary = extracted_info
		else:
			summary = Summarize.create_summary(data)

		return jsonify(summary)
	
	else:
		return jsonify({"error": "No data to summarize"})

if __name__ == '__main__':
	app.run(port=5500, debug=True)
	# app.run()