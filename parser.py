#!/usr/bin/env python
import sys, getopt
import json
import csv

def main(argv):

	inputfile = str(sys.argv[1])
	outputfile = str(sys.argv[2])

	# number of interested frequent ingredients
	frequent = int(sys.argv[3])

	fin = open(inputfile)
	data = json.load(fin) 
	fin.close()

	# create a list of all ingredients, dups allowed
	ingredients = list()
	for i in range(0, len(data)):
		for j in range(0, len(data[i]["ingredients"])):
			ingredients.append(data[i]["ingredients"][j].encode("utf-8"))

	counter = {}
	for ingredient in ingredients:
		if ingredient in counter:
			counter[ingredient] += 1
		else:
			counter[ingredient] = 1

	# ingredients in frequency descending order
	frequentIngredients = sorted(counter, key = counter.get, reverse = True)

	frequentIngredients = frequentIngredients[:frequent]

	# pprint(frequentIngredients)

	fout = open(outputfile, "wb+")
	writer = csv.writer(fout)
	# write header
	writer.writerow(['id', 'cuisine'] + frequentIngredients)
	# write entries

	for i in range(0, len(data)):
		row = list()
		row.append(data[i]["id"])
		cuisine = data[i].get('cuisine', '')
		row.append(cuisine.encode('utf-8'))

		items =  [x.encode('utf-8') for x in data[i]["ingredients"]]

		for j in range(0, len(frequentIngredients)):
			if frequentIngredients[j] in items:
				row.append(1)
			else:
				row.append(0)
		writer.writerow(row)
	fout.close()


if __name__ == "__main__":
   main(sys.argv[1:])