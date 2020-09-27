import json

class witObjects:

	def __init__(self, jsonResponse: json) -> None:
		"""
		Class contructor for witObjects
		:param jsonResponse: response from the wit.ai curl call.
		"""
		self.__reponse = jsonResponse
		self.__intents = jsonResponse["intents"][0]
		self.__entities = jsonResponse["entities"]

	def get_make_and_model(self) -> dict:
		"""
		Gets make and model from a message and sets them as class attributes
		:param entities: these are the entities which the make and model will be pulled from
		:return: Dictionary containing the make and model.
		"""
		try:
			return {"make": self.__entities["vehicle_make:vehicle_make"],
					"model": self.__entities["vehicle_model:vehicle_model"]}
		except:
			raise Exception("Failed to populate __make and __model in witObject class!")

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