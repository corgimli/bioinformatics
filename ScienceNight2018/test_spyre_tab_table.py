from spyre import server

import pandas as pd
from urllib.request import urlopen
import json
import seq_match

class StockExample(server.App):
	title = "Discover DNA Source"

	# inputs = [{
	# 	"type": 'dropdown',
	# 	"label": 'Company', 
	# 	"options": [
	# 		{"label": "Google", "value": "GOOG"},
	# 		{"label": "Yahoo", "value": "YHOO"},
	# 		{"label": "Apple", "value": "AAPL"}
	# 	],
	# 	"key": 'ticker', 
	# 	"action_id": "update_data"
	# }]
	inputs = [{
		"type": "text",
		"key": "words_1",
		"label": "Enter DNA Sequence",
		"value": "Example: CGCTAGCATCGTA", 
		"action_id": "update_data"
	}]

	controls = [{
		"type": "hidden",
		"id": "update_data"
	}]

	# tabs = ["Plot", "Table"]
	# tabs = ["Table"]

	outputs = [
		{
		# 	"type": "plot",
		# 	"id": "plot",
		# 	"control_id": "update_data",
		# 	"tab": "Plot"
		# }, { 
			"type": "table",
			"id": "table_id",
			"control_id": "update_data",
			# "tab": "Table",
			"on_page_load": True
		},
		{
		"type": "html",
		"id": "simple_html_output"
	}
	]

	def getHTML(self, params):
		# words = params["words_1"]
		return 'ERROR: No match found. Please re-enter DNA sequence'
		# return seq_match.match(words,0.5).to_json()

	def getData(self, params):
		# ticker = params['ticker']
		# # make call to yahoo finance api to get historical stock data
		# api_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=3m/json'.format(ticker)
		# result = urlopen(api_url).read()
		# data = json.loads(result.decode("utf8").replace('finance_charts_json_callback( ','')[:-1])  # strip away the javascript and load json
		# self.company_name = data['meta']['Company-Name']
		# df = pd.DataFrame.from_records(data['series'])
		# df['Date'] = pd.to_datetime(df['Date'],format='%Y%m%d')
		# return df
		words = params["words_1"]
		df = seq_match.match(words,0.5)
		if df.empty:
			self.getHTML(params)
		# return "Here's what you wrote in the textbox: <b>%s</b>" % words
		else:
			return df



	# def getPlot(self, params):
	# 	df = self.getData(params)#.set_index('Date').drop(['volume'],axis=1)
	# 	plt_obj = df.plot()
	# 	plt_obj.set_ylabel("Price")
	# 	# plt_obj.set_title(self.company_name)
	# 	fig = plt_obj.get_figure()
	# 	return fig

app = StockExample()
app.launch(port=9093)