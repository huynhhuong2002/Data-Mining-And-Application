import getopt, sys
import csv
from utils import*

def parseColumnParam(column_param):
	column_param=column_param.replace(' ','')
	column_param=column_param.replace('[','')
	column_param=column_param.replace(']','')
	column_param=column_param.split(',')
	return column_param

def parseMethodParam(method_param):
	method_param=method_param.replace(' ','')
	method_param=method_param.replace('[','')
	method_param=method_param.replace(']','')
	method_param=method_param.split(',')
	return method_param


output="normalizing_result.csv"
input_=""
method="z_score"
M=""
all_=False
min_=0
max_=1

cols=[]
methods=[]

# list of command line arguments
argumentList = sys.argv[1:]

#short options
options ="hi:c:m:M:a:o:mi:ma:"

#long options
long_options=["help", "input=", "column=", "method=", "METHOD=", "all=", "output=", "min=", "max="]

try:
	arguments, values = getopt.getopt(argumentList, options, long_options)

	if len(arguments)==1 and arguments[0][0] in ("-h", "--help"):
		helpMessageForNormalizeFunctions()
	else:
		for i in range(len(arguments)):
			if arguments[i][0] in ("-h", "--help"):
				helpMessageForNormalizeFunctions()
			elif arguments[i][0] in ("-i", "--input"):
				input_=str(arguments[i][1])
			elif arguments[i][0] in ("-o", "--output"):
				output=str(arguments[i][1])
			elif arguments[i][0] in ("-a", "--all"):
				if arguments[i][1]=="true":
					all_=True
				elif arguments[i][1]=="false":
					all_=False
				else:
					raise ValueError('unknown')	
			elif arguments[i][0] in ("-mi", "--min"):
				min_=float(arguments[i][1])
			elif arguments[i][0] in ("-ma", "--max"):
				max_=float(arguments[i][1])
			elif arguments[i][0] in ("-c", "--column"):
				cols=parseColumnParam(arguments[i][1])
			elif arguments[i][0] in ("-m", "--method"):
				methods=parseMethodParam(arguments[i][1])
			elif arguments[i][0] in ("-M", "--METHOD"):
				M=str(arguments[i][1])

		data=readDataset(input_)
		cols_of_data=getColumns(data)

		if all_:
			for c in cols_of_data:
				if c not in cols:
					cols.append(c)
		while len(methods)<len(cols):
			methods.append(method)

		if M!="" and M!='z_score' and M!='min_max':
			raise ValueError("unknown")

		if M=='z_score' or M=='min_max':
			methods=[]
			while len(methods)<len(cols):
				methods.append(M)

		for i in range(len(cols)):
			if cols[i] not in cols_of_data:
				raise ValueError("unknown")
			if methods[i]!='z_score' and methods[i]!='min_max':
				raise ValueError("unknown")

		for i in range(len(cols)):
			if methods[i]=='z_score':
				data[cols[i]]=Z_scoreNormalize(data,cols[i])
			else:
				data[cols[i]]=min_maxNormalize(data,cols[i],min_,max_)

		outputFile=open(output,'w',newline='')
		writer=csv.writer(outputFile)
		writer.writerow(cols_of_data)
		for i in range(getNumberOfSamples(data)):
			row=[]
			for c in cols_of_data:
				row.append(data[c][i])
			writer.writerow(row)
		print('Normalizing done, checking in ', output)
		outputFile.close()
except:
	showNotice()


	