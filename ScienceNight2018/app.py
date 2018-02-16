from spyre import server

import os
import pandas as pd
import seq_match

class Burger(server.App):
	title = "What is in your mystery soup?"

	inputs = [{
		"type": "text",
		"key": "words_1",
		"label": "Enter DNA Sequence",
		"value": "", 
		"action_id": "update_data"
	}]

	controls = [{
		"type": "hidden",
		"id": "update_data"
	}]

	outputs = [{
		"type": "table",
		"id": "table_id",
		"control_id": "update_data",
		"on_page_load": True
		},
		{
		"type": "html",
		"id": "simple_html_output",
		"control_id": "update_data",
		"on_page_load":True
	}]

	def getHTML(self, params):
		if self.getData(params).empty or not params["words_1"]:
			return "*** Please enter a valid DNA sequence. ***"
		else:
			return ""

	def getData(self, params):
		words = params["words_1"].upper()
		threshold = 0.5
		df = seq_match.match(words,threshold)
		return df

app = Burger()
# app.launch(port=9093)
app.launch(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))