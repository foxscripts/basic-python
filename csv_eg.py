import csv
with open('new.csv') as csvFile:
	readCSV = csv.reader(csvFile, delimiter=',')
	nations = []
	citizens = []
	for row in readCSV:
		nation = row[2]
		nations.append(nation)
		citizen = row[0]
		citizens.append(citizen)
	print(nations)
	print(citizens)

	nationality = input('Which nationalities citizen you wanna see? ')
	nIndex = nations.index(nationality.upper())

	theCitizen = citizens[nIndex]
	print(theCitizen)
