import pandas as pd 
import numpy as np
import math

def readDataset(fileName):
	data=pd.read_csv(fileName)
	return data

def showNotice():
	print('Adding -h/--help for instructions')

def basicHelpMessage():
	print('==============================================')
	print('|| DATA PREPROCESSING:                      ||')
	print('||                                          ||')
	print('|| -h/--help to show instructions           ||')
	print('|| -i/--input=... to input path to csv file ||')
	print('==============================================')

def helpMessageForRemovingFunctions():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -t/--threshold=... to input allowed threshold percentage of missing value           ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| DEFAULT THRESHOLD IS 0%, DEFAULT OUTPUT FILE PATH: "output.csv"                     ||')
	print('=========================================================================================')

def helpMessageForCalculateFunctions():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -f/--first=... to input first column you want to calculate                          ||')
	print('|| -s/--second=... to input second column you want to calculate                        ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| -m/--method=...(add/sub/mul/div) to calculate first and second column               ||')
	print('|| DEFAULT METHOD IS ADD, DEFAULT OUTPUT FILE PATH: "caculatation_result.csv"          ||')
	print('=========================================================================================')   

def helpMessageForFillMissingFunctions():
	print('========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -c/--column=... to input column you want to fill in                                 ||')
	print('|| -m/--method=...(mean/median/mode) to input method you want to use to fill in        ||')
	print('|| -a/--all=(true/false) to input if you want to fill all missing columns or not       ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| DEFAULT METHOD IS MEAN, DEFAULT OUTPUT FILE PATH: "filled_file.csv"                 ||')
	print('|| DEFAULT ALL: FALSE                                                                  ||')
	print('=========================================================================================')

def helpMessageForNormalizeFunctions():
	print('=========================================================================================')
	print('|| DATA PREPROCESSING:                                                                 ||')
	print('||                                                                                     ||')
	print('|| -h/--help to show instructions                                                      ||')
	print('|| -i/--input=... to input path to csv file                                            ||')
	print('|| -c/--column=["column1","column2",...] to input columns you want to normalize        ||')
	print('|| -m/--method=["method1","method2",...] to input methods you want to use to normalize ||')
	print('|| -a/--all=...(true/false) to input if you want to normalize all columns or not       ||')
	print('|| -M/--METHOD=...all selected columns are normalized by this method                   ||')
	print('|| -o/--output=... to output path to output file                                       ||')
	print('|| -mi/--min=... new min to normalize data (default: 0)                                ||')
	print('|| -ma/--max=... new max to normalize data (default: 1)                                ||')
	print('|| DEFAULT OUTPUT FILE PATH: "normalizing_result.csv"                                  ||')
	print('|| DEFAULT ALL: FALSE                                                                  ||')
	print('|| DEFAULT METHOD FOR NUMERICAL ATTRIBUTE: "z_score" (ALL methods: "z_score"/"min_max")||')
	print('|| DEFAULT -M is "" (empty string)                                                     ||')
	print('|| COLUMNS NAME MUST BE CONTAINED IN A LIST, SEPERATED BY ","                          ||')
	print('|| METHODS MUST BE CONTAINED IN A LIST, SEPERATED BY ","                               ||')
	print('|| IF A CATEGORICAL COLUMN IS PASSED, IT WILL BE IGNORE WHEN THE PROGRAM IS RAN        ||')
	print('=========================================================================================')
 
#get name of all columns in data 
def getColumns(data):
	return list(data)

#get the number of attributes in data
def getNumberOfAttributes(data):
	return len(getColumns(data))

#get the number of samples in data
def getNumberOfSamples(data):
	return len(data)

#check whether a value is null or not
def isNull(value):
	return value!=value 

#check whether a list contains null values or not
def isNullList(l):
	result=[isNull(value) for value in l]
	return True in result

#computing percentage of missing values in a row
def computePercentageOfMissingValuesInRow(data,row):
	sum_missing_values=0
	for c in getColumns(data):
		if isNull(data[c][row]):
			sum_missing_values+=1
	return (sum_missing_values/getNumberOfAttributes(data))*100

#computing percentage of missing values in a column
def computePercentageOfMissingValuesInColumn(data,column):
	sum_missing_values=0
	for i in range(getNumberOfSamples(data)):
		if isNull(data[column][i]):
			sum_missing_values+=1
	return (sum_missing_values/getNumberOfSamples(data))*100

#get type of a attribute in data
def typeOfAttribute(col,data):
	for i in range (getNumberOfSamples(data)):
		if isNull(data[col][i])==False:
			if type(data[col][i])==int or type(data[col][i])==np.int64 or type(data[col][i])==np.int32 or type(data[col][i])==float or type(data[col][i])==np.float64 or type(data[col][i])==np.float32:
				return 'numeric'
				break
			else:
				return 'categorical'
				break
	return 'none'

#get mean of a column in data
def meanOfCol(col,data):
	sum=0
	sample=0
	for i in range (getNumberOfSamples(data)):
		if isNull(data[col][i])==False:
			sample=sample+1
			sum=sum+data[col][i]
	mean=sum/sample
	return mean

#get standard deviation of a column in data
def stdOfCol(col,data):
	numberOfSamples = getNumberOfSamples(data)
	count_missing_values=0
	for i in range(numberOfSamples):
		if isNull(data[col][i]):
			count_missing_values+=1
	N=numberOfSamples-count_missing_values
	mean_=meanOfCol(col,data)
	variance = 0.0
	for i in range(numberOfSamples):
		if (isNull(data[col][i]) == False):
			variance +=float(pow(float(data[col][i]-mean_),2) / N)
	return math.sqrt(variance)

#get frequent of a value in a column
def freqOfValue(value,col,data):
	freq=0
	for i in range (getNumberOfSamples(data)):
		if data[col][i]==value:
			freq=freq+1
	return freq

def findMax(list_):
	maxValue=list_[0]
	for i in range (len(list_)):
		if list_[i]>maxValue:
			maxValue=list_[i]
	return maxValue

#get mode of a column in data		
def modeOfCol(col,data):
	value=[] #Value of Index i
	freq=[]  #List saves freq of Value of Index i
	for i in range (getNumberOfSamples(data)):
		if isNull(data[col][i])==False and (data[col][i] in value)==False:
			value.append(data[col][i])
			freq.append(freqOfValue(data[col][i],col,data))
	maxFreq=findMax(freq)
	for i in range (len(freq)):
		if value[i]==maxFreq:
			index=i
	return value[i]

#get median of a column in data
def medianOfCol(col,data):
	list_=[] #List saves not null values of this column
	for j in range (getNumberOfSamples(data)):
		if isNull(data[col][j])==False and (data[col][j] in list_)==False:
			list_.append(data[col][j])
	i=(len(list_)+1)/2
	list_.sort()
	if len(list_)%2!=0:
		return list_[i]
	else:
		return (list_[round(i)]+list_[round(i)-1])/2

#get min of a column in data
def minOfCol(col,data):
	numberOfSamples=getNumberOfSamples(data)
	min_=0
	for i in range(numberOfSamples):
		if isNull(data[col][i])==False:
			min_=data[col][i]
			break
	for i in range(numberOfSamples):
		if isNull(data[col][i])==False:
			if data[col][i]<min_:
				min_=data[col][i]
	return min_

#get max of a column in data
def maxOfCol(col,data):
	numberOfSamples=getNumberOfSamples(data)
	max_=0
	for i in range(numberOfSamples):
		if isNull(data[col][i])==False:
			max_=data[col][i]
			break
	for i in range(numberOfSamples):
		if isNull(data[col][i])==False:
			if data[col][i]>max_:
				max_=data[col][i]
	return max_

#filling missing values of a column in data
def fill_missing_valueOfCol(col,data,methods):
	fill=list(data[col])
	if methods=='mean':
		x=meanOfCol(col,data)
		for i in range(getNumberOfSamples(data)):
			if isNull(fill[i]):
				fill[i]=x
	elif methods=='median':
		x=medianOfCol(col,data)
		for i in range(getNumberOfSamples(data)):
			if isNull(fill[i]):
				fill[i]=x
	else:
		x=modeOfCol(col,data)
		for i in range(getNumberOfSamples(data)):
			if isNull(fill[i]):
				fill[i]=x
	return fill

#get index of a attribute in list of data's attributes
def findIndexOfCol(col,data):
	title=getColumns(data)
	for i in range(len(title)):
		if title[i]==col:
			return i

#check right filling method for numerical and categorical attributes
def checkMethod(method,col,data):
	if typeOfAttribute(col,data)=='numeric':
		if method=='mean' or method=='median':
			return True
		else: return False
	elif typeOfAttribute(col,data)=='categorical':
		if method=='mode':
			return True
		else:
			return False
	return False
	   
#add two columns
def add(numA,numB):
	if isNull(numA)==False and isNull(numB)==False:
		return numA+numB
	else:
		if isNull(numA)==True:
			return numA
		else:
			return numB

#subtract two columns		
def sub(numA,numB):
	if isNull(numA)==False and isNull(numB)==False:
		return numA-numB
	else:
		if isNull(numA)==True:
			return numA
		else:
			return numB

#multiply two columns
def mul(numA,numB):
	if isNull(numA)==False and isNull(numB)==False:
		return numA*numB
	else:
		if isNull(numA)==True:
			return numA
		else:
			return numB

#divide two columns		
def div(numA,numB):
	if isNull(numA)==False and isNull(numB)==False:
		return numA/numB
	else:
		if isNull(numA)==True:
			return numA
		else:
			return numB

#normalize columns by Z-score method
def Z_scoreNormalize(data,col):
	if typeOfAttribute(col,data)!='numeric':
		return data[col]  
	else:
		mean_=meanOfCol(col,data)
		std=stdOfCol(col,data)
		result = []
		for i in range(getNumberOfSamples(data)):
			if isNull(data[col][i]):
				result.append(data[col][i])
			else:
				result.append(round(float((float(data[col][i])-mean_)/std),4))
		return result

#normalize columns by min-max method
def min_maxNormalize(data,col,newMin,newMax):
	if typeOfAttribute(col,data)!='numeric':
		return data[col]
	else:
		min_=minOfCol(col,data)
		max_=maxOfCol(col,data)
		std=stdOfCol(col,data)
		result = []
		for i in range(getNumberOfSamples(data)):
			if isNull(data[col][i]):
				result.append(data[col][i])
			else:
				result.append(round(float((float(data[col][i])-min_)/(max_-min_)*(newMax-newMin) + newMin),4))
		return result

