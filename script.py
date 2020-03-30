import requests
import json

from wiktionaryparser import WiktionaryParser

def getBook():
	response = requests.get("http://corpus-db.org/api/id/2759.0/fulltext")
	return response.json()[0]["text"]

def getMetadata():
	response = requests.get("http://corpus-db.org/api/id/2759.0")

	return response.json()

def getDefinition(word):
	parser = WiktionaryParser()
	data = parser.fetch(word)
	return data