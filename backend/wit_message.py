import json

class witObjects:

	__reponse = None
	__intents = None
	__entities = None

	def __init__(self, jsonResponse: json) -> None:
		"""
		Class contructor for witObjects
		:param jsonResponse: response from the wit.ai curl call.
		"""
		self.__reponse = jsonResponse
		self.__intents = jsonResponse["intents"][0]
		self.__entities = jsonResponse["entities"]

	def get_response(self) -> json:
		"""
		Returns string containing the intent of the message from wit.ai json reponse
		:param jsonResponse: json file
		:return: a json which is the intent of the message.
		"""
		return self.__reponse


	def get_intents(self) -> json:
		"""
		Returns string containing the intent of the message from wit.ai json reponse
		:param jsonResponse: json file
		:return: a json which is the intent of the message.
		"""
		return self.__intents

	def get_entities(self) -> json:
		"""
		Returns string containing the intent of the message from wit.ai json reponse
		:param jsonResponse: json file
		:return: a json which is the entities of the file
		"""
		return self.__entities


if __name__ == '__main__':
	import response
	import json

	response = witObjects(response.get_response_wit("i want to buy a porsche 911"))

	print(response.get_intents())
	print(response.get_entities())
	print(response.get_response())

	# print(json.dumps(response, indent=4, sort_keys=True))