import getopt, sys
from utils import*

# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:"

#long options
long_options=["help", "input="]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	if len(arguments)==1 and arguments[0][0] in ("-h", "--help"):
		basicHelpMessage()
	else:
		for i in range(len(arguments)):
			if arguments[i][0] in ("-h", "--help"):
				basicHelpMessage()
			elif arguments[i][0] in ("-i", "--input"):
				num_missing_rows=0
				data=readDataset(str(arguments[i][1]))
				columns= getColumns(data)
				for j in range(getNumberOfSamples(data)):
					for c in columns:
						if isNull(data[c][j]):
							num_missing_rows+=1
							break
				print('The number of rows that have missing values: ', num_missing_rows)
except:
	showNotice()

