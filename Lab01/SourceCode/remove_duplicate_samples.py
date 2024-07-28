import getopt, sys
import csv
from utils import*

def helpMessage():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| DEFAULT OUTPUT FILE PATH: "output.csv"                                              ||')
	print('=========================================================================================')

output="output.csv"
input_=""

# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:o:"

#long options
long_options=["help", "input=", "output="]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	if len(arguments)==1 and arguments[0][0] in ("-h", "--help"):
		helpMessage()
	else:
		for i in range(len(arguments)):
			if arguments[i][0] in ("-h", "--help"):
				helpMessage()
			elif arguments[i][0] in ("-i", "--input"):
				input_=str(arguments[i][1])
			elif arguments[i][0] in ("-o", "--output"):
				output=str(arguments[i][1])

		outputFile=open(output,'w',newline='')
		writer=csv.writer(outputFile)

		data=readDataset(input_) #for DataFrame Structure to use functions in utils.py
		num_of_samples=getNumberOfSamples(data)

		writer.writerow(getColumns(data)) #write columns name
		columns=getColumns(data)
		rows=[]
		rows2=[]
		for i in range(num_of_samples):
			row=[]
			row2=[]
			for c in columns:
				row.append(data[c][i])
				if isNull(data[c][i]):
					row2.append(-82)
				else:
					row2.append(data[c][i])
			if row2 not in rows2:
				writer.writerow(row)
				rows.append(row)
				rows2.append(row2)
		print('Removing done, checking in ', output)
		print('The number of removed samples: ', num_of_samples-len(rows))
		outputFile.close()
except:
	showNotice()