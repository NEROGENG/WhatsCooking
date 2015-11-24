#!/usr/bin/env python
import sys
import csv
import numpy

def main(argv):

	inputfile = str(sys.argv[1])
	trainfile = str(sys.argv[2])
	testfile = str(sys.argv[3])
	trainPercent = float(sys.argv[4])

	fin = open(inputfile, 'rb')
	reader = csv.reader(fin)

	# list of lists 
	data = list()
	for row in reader:
		data.append(row)

	header = data[0]
	data.remove(data[0])

	# shuffle entries
	numpy.random.shuffle(data)
	splitIndex = int(len(data) * trainPercent)

	# split data into training set and test set
	training, test = data[:splitIndex], data[splitIndex:]
	fin.close()

	ftrain = open(trainfile, "wb+")
	writer = csv.writer(ftrain)
	writer.writerow(header)
	writer.writerows(training)
	ftrain.close()

	ftest = open(testfile, "wb+")
	writer = csv.writer(ftest)
	writer.writerow(header)
	writer.writerows(test)
	ftest.close()

if __name__ == "__main__":
   main(sys.argv[1:])