import getopt, sys
import csv
from utils import*

threshold=0
output="output.csv"
input_=""

# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:t:o:"

#long options
long_options=["help", "input=", "threshold=","output="]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	if len(arguments)==1 and arguments[0][0] in ("-h", "--help"):
		helpMessageForRemovingFunctions()
	else:
		for i in range(len(arguments)):
			if arguments[i][0] in ("-h", "--help"):
				helpMessageForRemovingFunctions()
			elif arguments[i][0] in ("-i", "--input"):
				input_=str(arguments[i][1])
			elif arguments[i][0] in ("-t", "--threshold"):
				threshold = arguments[i][1]
			elif arguments[i][0] in ("-o", "--output"):
				output=str(arguments[i][1])

		outputFile=open(output,'w',newline='')
		writer=csv.writer(outputFile)

		data=readDataset(input_) #for DataFrame Structure to use functions in utils.py
		num_of_samples=getNumberOfSamples(data)

		writer.writerow(getColumns(data)) #write columns name
		columns=getColumns(data)
		sumOfRemovedRows=[]
		for i in range(num_of_samples):
			if computePercentageOfMissingValuesInRow(data,i) < float(threshold):
				row=[]
				for c in columns:
					row.append(data[c][i])
				writer.writerow(row)
				sumOfRemovedRows.append(row)
		print('Removing done, checking in ', output)
		print('The number of removed rows: ', num_of_samples-len(sumOfRemovedRows))
		outputFile.close()
except:
	showNotice()