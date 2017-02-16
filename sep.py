import csv
import time
import datetime

with open('Crime_Incidents_Condensed.csv', mode='r') as infile:
	with open('Crime_Incidents_Cleaned_14-16.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		reader = csv.reader(infile)
                headers = 0
		for row in reader:
                    #if we haven't written the headers yet, do that
                    if headers == 0:
                        headers = 1
                        writer.writerow(row)
                    #make sure there is a date committed
                    elif row[4]:
                        #tstamp = datetime.datetime.strptime(row[4],"%m/%d/%y %H:%M")
                        tstamp = datetime.datetime.strptime(row[4],"%Y-%m-%d %H:%M")
                        block = row[5] + '_' + row[6] + '_' + row[7]
                        doy = tstamp.timetuple().tm_yday
                        row[14] = tstamp.year
                        row[15] = tstamp.month
                        row[16] = tstamp.day
                        row[17] = tstamp.weekday()
                        row[18] = doy
                        row[19] = tstamp.time()
                        row[20] = tstamp.hour
                        row[21] = block
                        if row[14] == 2016 or row[14] == 2015 or row[14] == 2014:
                            print row
                            writer.writerow(row)
        outfile.close()
infile.close()

