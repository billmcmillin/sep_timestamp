import csv
import time
import datetime
import re

with open('Crime_Incidents_Condensed.csv', mode='r') as infile:
	with open('all_crimes.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		reader = csv.reader(infile)
		seenCrimes = []	
		crimeTuple = [0,0]
		for row in reader:
			crime = re.split('[A-Z]', row[2])[0]
			if crime not in seenCrimes:
				seenCrimes.append(crime)
				print crime
				crimeTuple[0] = crime
				crimeTuple[1] = row[1]
				writer.writerow(crimeTuple)
	outfile.close()
infile.close()

