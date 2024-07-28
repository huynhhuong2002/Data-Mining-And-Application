import getopt, sys
import csv
from utils import*

input_=""
method='add'
columnA=""
columnB=""
output="caculated_result.csv"
# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:f:s:m:o:"

#long options
long_options=["help", "input=","first=","second=","method=","output="]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	if len(arguments)==1 and arguments[0][0] in ("-h", "--help"):
		helpMessageForCalculateFunctions()
	else:
		for i in range(len(arguments)):
			if arguments[0][0] in ("-h", "--help"):
				helpMessageForCalculateFunctions()
			elif arguments[i][0] in ("-i", "--input"):
				input_=str(arguments[i][1])
			elif arguments[i][0] in ("-m", "--method"):
				method = arguments[i][1]
			elif arguments[i][0] in ("-f", "--first"):
				columnA = arguments[i][1]
			elif arguments[i][0] in ("-s", "--second"):
				columnB = arguments[i][1]
			elif arguments[i][0] in ("-o", "--output"):
				output=str(arguments[i][1])

		outputFile=open(output,'w',newline='')
		writer=csv.writer(outputFile)

		data=readDataset(input_) #for DataFrame Structure to use functions in utils.py
		num_of_samples=getNumberOfSamples(data)

		titles=getColumns(data) #list saves name of tittles
		typeTitles=[] #list save type of tittles

		for i in range (len(titles)):
			x=typeOfAttribute(titles[i],data)
			typeTitles.append(x)

		indexColA=findIndexOfCol(columnA,data)
		indexColB=findIndexOfCol(columnB,data)

		#Neu columnA va columnB la categorical thi bao loi
		if typeTitles[indexColA]=='categorical' or typeTitles[indexColB]=='categorical':
			print('Please check type of these two column again')
			print(output,' is empty cause type of these column are unresonable')
		elif typeTitles[indexColA]=='numeric' or typeTitles[indexColB]=='numeric':
			rows=[]
			rows.append(['Result'])
			if method=='add':
				for i in range(num_of_samples):
					x=add(data[columnA][i],data[columnB][i])
					rows.append([x])
				writer.writerows(rows)
			elif method=='sub':
				for i in range(num_of_samples):
					x=sub(data[columnA][i],data[columnB][i])
					rows.append([x])
				writer.writerows(rows)
			elif method=='mul':
				for i in range(num_of_samples):
					x=mul(data[columnA][i],data[columnB][i])
					rows.append([x])
				writer.writerows(rows)
			elif method=='div':
				for i in range(num_of_samples):
					x=div(data[columnA][i],data[columnB][i])
					rows.append([x])
				writer.writerows(rows)
			print('Calculating done, checking in ', output)
		
		outputFile.close()
except:
	showNotice()
