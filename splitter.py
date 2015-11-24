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
	reader = csv.reader(fin, delimiter=' ', quotechar='|')

	header = reader[0]

	reader = reader[1:len(reader)]
	numpy.random.shuffle(reader)
	training, test = reader[:80,:], reader[80:,:]
	fin.close()

	ftrain = open(trainfile, "wb+")
	writer = csv.writer(fout)
	writer.writerow(header)
	writer.writerows(training)

if __name__ == "__main__":
   main(sys.argv[1:])