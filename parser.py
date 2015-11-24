#!/usr/bin/env python
import sys
import json
import csv
from pprint import pprint

f = open('train.json') 
data = json.load(f) 
f.close()

# create a list of all ingredients, dups allowed
ingredients = list()
for i in range(0, len(data)):
	for j in range(0, len(data[i]["ingredients"])):
		ingredients.append(data[i]["ingredients"][j].encode("utf-8"))

# number of interested frequent ingredients
frequent = 300

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

writer = csv.writer(open("test.csv", "wb+"))
# write header
writer.writerow(['id', 'cuisine'] + frequentIngredients)
# write entries
for i in range(0, len(data)):
	row = list()
	row.append(data[i]["id"])
	row.append(data[i]["cuisine"].encode('utf-8'))

	items =  [x.encode('utf-8') for x in data[i]["ingredients"]]

	for j in range(0, len(frequentIngredients)):
		if frequentIngredients[j] in items:
			row.append(1)
		else:
			row.append(0)
	writer.writerow(row)
