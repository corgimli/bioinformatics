from spyre import server
import seq_match

class SimpleApp(server.App):
	title = "Simple App"
	inputs = [{
		"type": "text",
		"key": "words_1",
		"label": "write words here",
		"value": "hello world", 
		"action_id": "simple_html_output"
	}]

	outputs = [{
		"type": "html",
		"id": "simple_html_output"
	}]

	def getHTML(self, params):
		words = params["words_1"]
		# return "Here's what you wrote in the textbox: <b>%s</b>" % words
		return seq_match.match(words,0.5).to_json()

app = SimpleApp()
app.launch()