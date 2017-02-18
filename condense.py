import csv
import time
import datetime

with open('Master_Cleaned.csv', mode='r') as infile:
	with open('Monthly.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		reader = csv.reader(infile)
                #we're creating a monthly report that contains the following fields:
                #neighborhood year month count
                headers = ['neighborhood', 'year', 'month','count'] 
                #create a dict for neighborhoods
                nabes = []
                repArs = []
                years = []
                months = []
                reports = {} 
                header = 0
                crimes = []
                okYears = ['2010','2011','2012','2013','2014','2015','2016','2017']
                for row in reader:
                    if header == 0:
                        header += 1
                        continue
                    crimes.append(row)
                    if row[11] not in nabes:
                        nabes.append(row[11])
                        #print row[11]
                    if row[14] in okYears and row[14] not in years:
                        years.append(row[14])
                    if row[15] not in months:
                        months.append(row[15])
                    if row[10] not in repArs:
                        repArs.append(row[10])
                    #reports[row[11]] += 1 
                
                #create dict for reports
                #report_dict = {('neighborhood','2012','10'): 3
                #writer.writerow(row)
                #reports = {va[11]: 0 for va in reader}
        outfile.close()
infile.close()

with open('Monthly.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for year in years:
        for month in months:
            for nabe in nabes:
                count = 0
                murder = 0
                for crime in crimes:
                    if crime[14] == year and crime[15] == month and crime[11] == nabe:
                        count +=1
                        if crime[12] == '105' or crime[12] == '101':
                            murder += 1
                report = [year,month,nabe,count,murder]
                writer.writerow(report)
                print report
outfile.close()
