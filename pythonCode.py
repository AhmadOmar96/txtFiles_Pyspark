
#this is a solved of the same problem without spark and read from zip file

from zipfile import ZipFile

zipReader = ZipFile('txtFiles.zip')
files = [zipReader.read(name) for name in zipReader.namelist()]
content = ""
listsOfNames = []
names = []
listResults = []
for file in files:
    content = file.decode("utf-8")
    names = content.split()
    if len(names) > 0:
        listsOfNames.append(names)

print("\n\n********** The Names From Files **********")
print(listsOfNames)
filesCount = len(listsOfNames)
flg = 0

for lstNames in listsOfNames:
    for name in lstNames:
        for n in range(0, len(listResults)):
            if name in listResults[n]:
                flg = 1
                break
        if flg == 1:
            continue
        counter = 0
        for i in range(0, filesCount):
            if name in listsOfNames[i]:
                counter += 1
        if counter == filesCount:
            listResults.append([name, counter])


for i in range(0, len(listResults)):
    counter = 0
    for lstNames in listsOfNames:
        for name in lstNames:
            if name == listResults[i][0]:
                counter += 1
                listResults[i][1] = counter

print("\n\n********** Existed Names in All Files And its Count **********")
print(listResults)



