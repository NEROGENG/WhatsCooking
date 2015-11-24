#!/usr/bin/env python

import json
import csv
#from pprint import pprint

f = open('train.json') 
data = json.load(f) 
f.close()

print(len(data))