from flask import Flask, render_template, request
from script import getBook, getMetadata, getDefinition

app = Flask(__name__)

@app.route("/")
def hello():
	return book()

@app.route("/book", methods=['GET', 'POST'])
def book():
	word = definition = link = ''

	if request.method == 'POST' and request.form['word'] != '':
		word = request.form['word']
		data = getDefinition(word.lower())
		if len(data) > 0:
			try:
				definition = data[0]["definitions"][0]
			except IndexError:
				definition = ''
		link = "https://en.wiktionary.org/wiki/" + word

	metadata = getMetadata()
	return render_template("book.html", 
		text=getBook(), 
		author=metadata["author"], 
		title=metadata["title"], 
		word=word, 
		link=link,
		definition=definition)

if __name__ == "__main__":
	app.run()