import csv
import pprint


def get_tags_and_index():

	with open('vehicles.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		dict = {}
		for row in readCSV:
			for element in row:
				dict[str(element)] = row.index(element)
			break
		return dict

def dict_of_brands():

	with open('vehicles.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		make_index = get_tags_and_index()['make']
		dict = {}
		makes = []
		entry_coutns = 0

		for row in readCSV:
			makes.append(row[make_index])
			# print(row)
			++entry_coutns
		makes = set(makes)
		for m in makes:
			dict[m] = []
			for row in readCSV:
				if m in row:
					dict[m].append(row)


		pprint.pprint(dict)


if __name__ == '__main__':

	dict_of_brands()