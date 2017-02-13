import csv
import time
import datetime

with open('Crime_Incidents_Condensed.csv', mode='r') as infile:
	with open('Crime_Incidents_Cleaned_2016.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		reader = csv.reader(infile)
                headers = 0
		for row in reader:
                    #if we haven't written the headers yet, do that
                    if headers == 0:
                        headers = 1
                        writer.writerow(row)
                    elif row[4]: 
                        tstamp = datetime.datetime.strptime(row[4],"%m/%d/%y %H:%M")
                        print tstamp.time()
                        row[14] = tstamp.year
                        row[15] = tstamp.month
                        row[16] = tstamp.day
                        row[17] = tstamp.weekday()
                        row[18] = tstamp.time()
                        row[19] = tstamp.hour
                        if row[14] == 2016:
                            writer.writerow(row)
        outfile.close()
infile.close()

