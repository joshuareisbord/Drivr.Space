import csv
import json
import pprint


def get_tags_and_index_from_master_list(write_to_json=False) -> dict:
	"""
	Gets a list of keys and their respective index relative to the vehicle entries in vehicles.csv
	:param write_to_json: Write dictionary to json file if true. Useful for testing.
	:return: dictionary of keys and there index values in in vehicles.csv
	"""
	with open('vehicles.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		dictionary = {}
		for row in readCSV:
			for element in row:
				dictionary[str(element)] = row.index(element)
			break

		# Write dictionary to json file
		if write_to_json:
			with open("tags_and_index.json", "w") as file:
				json.dump(dictionary, file, sort_keys=False, indent=2)

		# Return the dictionary of all the tags and their index positions
		return dictionary


def create_sorted_dict_of_models_by_brand(write_to_json=False) -> dict:
	"""
	Sorts vehicles in vehicles.csv into their respective keys based on make make, and writes to data.json
	:param write_to_json: Write dictionary to json file if true. Useful for testing.
	:return: dictionary
	"""
	with open('vehicles.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		make_index = get_tags_and_index_from_master_list()['make']
		csvEntries = []
		dict = {}
		makes = []

		# Creates a list of all makes of vehicles in the database
		for row in readCSV:
			csvEntries.append(row)
			makes.append(row[make_index])
		makes = set(makes)

		# Creates a key for each make in a dictionary
		for m in makes:
			dict[m] = None

		# Create a list of all entries which contain the vehicle make, and then assign to dictionary keys
		for key in dict.keys():
			lst = []
			# print(key)
			for row in csvEntries:
				if key in row:
					lst.append(row)
				dict[key] = tuple(lst)
			lst = []

		# Write all data to a json file
		if write_to_json:
			with open("data.json", "w") as file:
				json.dump(dict, file, sort_keys=False, indent=2)

		# Return the dictionary of sorted vehicles based on make
		return dict


def get_all_models_by_make(make: str) -> dict:
	"""
	Get all models by a specific make of vehicles
	:param make: String which is the make of vehicles being looked for
	:return: dictionary containing load result, and data from the file
	"""

	# Try load all the vehicles into a dictionary
	try:
		data = create_sorted_dict_of_models_by_brand()
		# Pull all the vehicles from a make of automobiles.
		try:
			make_models = data[make]
			return {"success": True, "models": [make_models]}
		# Specified make was not found in the file
		except:
			return {"success": False, "models": [None]}
	# JSON file could not be loaded or was not present.
	except:
		raise Exception("Unable to load vehicle data!")


def get_specific_model(model_to_find: str, models: dict, exact_model=False) -> dict:
	"""
	Returns a dictionary of models from the provided
	:param model: Model name of vehicle being looked for
	:param models: dicationary containing two keys, sucesss of get_all_models_by_make and the list of models.
	:param exact_model: Does the search need to be for the exact model name or can it contain the model name
	:return: returns the list of exact models or models which contain the model name
	"""
	# There are models contained in the dictionary

	toReturn = {"sucess": False, "models": None}
	vehicle_make_index = get_tags_and_index_from_master_list()["model"]

	# If the models arg contains models from a specific make
	if models["success"]:
		found_models = []

		for current_vehicle in models["models"][0]:  # Search through all of the vehicles in the models dictionary

			# Look for exact model name
			if exact_model:
				# print("Looking for exact model")
				if current_vehicle[vehicle_make_index] == model_to_find:
					found_models.append(current_vehicle)
					toReturn["success"] = True
				else:
					continue

			# Look for approximate model name
			else:
				# print("Not looking for exact model")
				if model_to_find in current_vehicle[vehicle_make_index]:
					found_models.append(current_vehicle)
					toReturn["success"] = True
				else:
					continue
	# The previous search was unsuccessful. There are no vehicles in the models.
	else:
		return toReturn

	# Was there vehicles added to found_models
	if len(found_models) != 0:
		toReturn["models"] = found_models  # Add the found vehicles to the

	return toReturn

if __name__ == '__main__':

	try:
		print(json.dumps(get_specific_model("Aztek", get_all_models_by_make("Pontiac"), exact_model=False), indent=True))

	except:
		create_sorted_dict_of_models_by_brand(write_to_json=True)
		get_tags_and_index_from_master_list(write_to_json=True)


