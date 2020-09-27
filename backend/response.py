from wikipedia import WikipediaPage
import wolframalpha
import json
import wikipedia
import wit

witClient = wit.Wit("DTIBACFI5NLIEIR7EOAHBGDNKTYXEA2A")
wolframalphaClient = wolframalpha.Client("QAT4UH-YT4UEQW94X")


def get_response_wikipedia(page: str) -> str:
	"""
	Returns a page object containing all information of a Wikipedia page
	:param page: String which is a valid wikipedia page
	:return: WikipediaPage object
	"""
	return wikipedia.page(wikipedia.search(page)[0]).summary


def get_response_wolframaplha(message: str) -> wolframalpha.Result:
	"""
	Accepts a message in string format and responds with the response in JSON format from Wit.ai
	:param message: message to be sent to wit.ai for processing
	:return: json containing intent in the message
	"""
	return wolframalphaClient.query(message)


def get_response_wit(message: str) -> json:
	"""
	Accepts a message in string format and responds with the response in JSON format from Wit.ai
	:param message: message to be sent to wit.ai for processing
	:return: json containing intent in the message
	"""
	return witClient.message(message)


if __name__ == '__main__':
	search_phrase = "Porsche 911"
	response = get_response_wikipedia(search_phrase)
	print(response)

	import json
	response = get_response_wit("i want to learn about the porsche 911")
	print(json.dumps(response, indent=4))

