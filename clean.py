import csv
import time
import datetime
import os
import sys
import re

#http://stackoverflow.com/questions/20078816/replace-non-ascii-characters-with-a-single-space/20079244#20079244
def printable(s):	
	re.sub(r'[^\x00-\x7f]',r' ',s)
	return s

fi = sys.argv[1]
fo = sys.argv[2]
with open(fi, mode='r') as infile:
	with open(fo, mode='w') as outfile:
		with open('outliers.csv',mode='w') as outliers:
			outliers_writer = csv.writer(outliers)
			writer = csv.writer(outfile)
			reader = csv.reader(infile)
			i = 0	
			for row in reader:
				i += 1
				#row[0] = CASE_REPORT_NO 
				if row[0] == '': 
					#print 'null case' + str(i)
					outliers_writer.writerow(row)	
					continue
				else:
					#make sure it's only utf-8 with no leading or trailing spaces
					row[0] = printable(row[0]).strip()
				if row[1] == '': 
					#print 'null case' + str(i)					
					outliers_writer.writerow(row)	
					continue
				else:
					row[1] = printable(row[1]).strip()
				if row[2] == '': 
					#print 'null case' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[2] = printable(row[2]).strip()
				#check for a valid timestamp	
				try:
					tm = time.strptime(row[3], "%Y-%m-%d %H:%M")
				except ValueError:
					tm = ''	
				if tm == '': 
					print 'null time' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[3] = printable(row[3]).strip() 
				#check for a valid timestamp	
				try:
					tm = time.strptime(row[4], "%Y-%m-%d %H:%M")
				except ValueError:
					tm = ''	
				if tm == '': 
					print 'null time' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[4] = printable(row[4]).strip() 
				if row[5] == '': 
					#print 'null case' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[5] = printable(row[5]).strip()
				if row[6] == '': 
					#print 'null case' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[6] = printable(row[6]).strip()
				if row[7] == '': 
					#print 'null case' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[7] = printable(row[7]).strip()
				#validate the district value
				districts = ['1','2','3','4','5','central business']
				if row[8] == '' or not row[8].lower() in districts: 
					print row[8]
					outliers_writer.writerow(row)
					continue
				else:
					row[8] = printable(row[8]).strip()
				beats = ['1','2','3','4','5','6']
				if row[9] == '' or not row[9] in beats: 
					print row[9]
					outliers_writer.writerow(row)
					continue
				else:
					row[9] = printable(row[9]).strip()
				#reporting area
				try: 
					repArea = int(row[10])
				except:
					print "invalid value"	
				if repArea == '':
					print 'null case' + str(i)
					outliers_writer.writerow(row)
					continue
				else:
					row[10] = printable(row[10]).strip()
				neighb = row[11].lower()
				if neighb == '':
					outliers_writer.writerow(row)
					continue
				else:
					row[11] = printable(neighb).strip()
				if row[12] == '':
					outliers_writer.writerow(row)
					continue
				else:
					row[12] = printable(row[12]).strip()
				#row 13 has lots of null values, leave it alone
				for n in range(14,21):
					if row[n] == '':
						outliers_writer.writerow(row)
						continue
					else:
						row[n] = printable(row[n]).strip()
				writer.writerow(row)	
		outliers.close()		
	outfile.close()
infile.close()

