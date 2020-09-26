import json

def get_intents(jsonReponse: json) -> json:
	"""
	Returns string containing the intent of the message from wit.ai json reponse
	:param jsonReponse: json file from main.get_reponse()
	:return: a json which is the intent of the message.
	"""
	return jsonReponse["intents"]

def get_entities(jsonReponse: json) -> json:
	"""
	Returns string containing the intent of the message from wit.ai json reponse
	:param jsonReponse: json file from main.get_reponse()
	:return: a json which is the entities of the file
	"""
	return jsonReponse["entities"]


if __name__ == '__main__':
	import get_response
	import json

	response = get_response.get_response_wit("Give me information on the porsche 911")
	print(json.dumps(response, indent=4, sort_keys=True))