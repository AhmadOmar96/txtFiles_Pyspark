import glob
from pyspark.sql import SparkSession

#build new spark session
spark = SparkSession.builder.appName("prog").master("local").getOrCreate()
#read files paths
filesPaths = glob.glob("txtFiles/*.txt")
#creat a list o dataframe which contain dataframe of each file will be read by spark
dataframeFiles = []
#read files with spark to datafram
for path in filesPaths:
    dataframeFiles.append(spark.read.text(path))
#this list will contain the result of search
listResults = []
#this flag to skip the loop if we detect the name before
flg = 0
for file in dataframeFiles: #loop for files
    for name in file.collect(): #loop for names in file
        for n in range(0, len(listResults)): #loop to check if we passed the name before
            if name[0] in listResults[n]:
                flg = 1
                break
        if flg == 1:
            continue
        counter = 0
        for i in range(0, len(dataframeFiles)): #loop for files count
            if name in dataframeFiles[i].collect(): #check if the name exist in the other files
                counter += 1
        if counter == len(dataframeFiles):
            listResults.append([name[0], counter])#save the name if exist in all files
#this loops to count the result in all files
for i in range(0, len(listResults)):
    counter = 0
    for file in dataframeFiles:
        for name in file.collect():
            if str(name[0]) == str(listResults[i][0]):
                counter += 1
                listResults[i][1] = counter

#show the original files
print("\n\n********** The Files **********")
for file in dataframeFiles:
    file.show()

#to show the result as list
print("\n\n********** Output File as list **********")
print(listResults)

#creat new dataframe for the results and show it
#columns = ["Name", "Count"]
#outputDataFrame = spark.createDataFrame(data=listResults, schema=columns)
#print("\n\n********** Output File **********")
#outputDataFrame.show()
