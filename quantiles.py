import csv
import numpy as np

with open('Monthly.csv', mode='r') as infile:
    reader = csv.reader(infile)
    #input fields:
    headers = ['year','month','neighborhood','crimes','murders','city_quart','neighb_quar']
    #create a dict for neighborhoods
    nabes = []
    years = []
    months = []
    header = 0
    crimes = []
    #we don't want 2010 or 2017 because they're incomplete
    okYears = ['2011','2012','2013','2014','2015','2016']
    for row in reader:
        if header == 0:
            header += 1
            continue
        #create a list of all observations to loop through again
        if row[2] not in nabes:
            nabes.append(row[2])
        if row[0] in okYears and row[0] not in years: 
            years.append(row[0])
        if row[1] not in months:
            months.append(row[1]) 
        if row[0] in okYears:
            row[3] = int(row[3])
            crimes.append(row)
infile.close()

#create a dict of the city-wide crime counts for each month - {('2015','02'): [25,323,12]}

#create a dict of all monthly crime counts for each neighborhood {'Clifton': [35,12,19]}
nabedict = {n : [] for n in nabes}

keys = []
for year in years:
    for mon in months:
       keys.append((year,mon))

monthdict = {mon : [] for mon in keys}


for crime in crimes:
    nabedict[crime[2]].append(crime[3])
    monthdict[(crime[0],crime[1])].append(crime[3])

#determine the quartiles of the two lists and store in a dict
nabe_quarts = {n : [] for n in nabes}
month_quarts = {m : [] for m in monthdict}
#build a dictionary with each neighborhood as the key and the quartiles in list form as value
for n in nabes:
    ar = np.array(nabedict[n])
    first = np.percentile(ar,25)
    second = np.percentile(ar,50)
    third = np.percentile(ar,75)
    nabe_quarts[n] = [first,second,third]

#
#build a dictionary with each year/month as the key and the quartiles in list form as value
for key in monthdict:
    ar = np.array(monthdict[key])
    first = np.percentile(ar,25)
    second = np.percentile(ar,50)
    third = np.percentile(ar,75)
    month_quarts[key] = [first,second,third]

#function to return the quartile of a given value
def get_quartile(num_crimes, quartiles):
    #check for first quartile
    if num_crimes <= quartiles[0]:
        q = 1
    elif num_crimes <= quartiles[1]:
        q = 2
    elif num_crimes <= quartiles[2]:
        q = 3
    else: 
        q = 4
    return q

with open('quarts.csv', mode='wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    for crime in crimes:
        key = (crime[0],crime[1])
        city_quart = get_quartile(crime[3],month_quarts[key])
        crime.append(city_quart)
        neighb_quart = get_quartile(crime[3],nabe_quarts[crime[2]])
        crime.append(neighb_quart)
        #print crime
        #print str(neighb_quart) + ' ' + str(crime[3]) + '' + str(nabe_quarts[crime[2]])
        writer.writerow(crime)

