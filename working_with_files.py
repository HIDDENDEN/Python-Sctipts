inFile = open("input.txt", 'r', encoding="utf8")
outFile = open("output.txt", "w", encoding="utf8")
lines = inFile.readlines()
listOfLists = list()
for line in lines:
    myList = list(map(str, line.split()))
    listOfLists.append(myList)
listOfLists.sort(key=lambda x: x[0])
for i in listOfLists:
    print(i[0], i[1], i[3], file=outFile)
inFile.close()
outFile.close()
