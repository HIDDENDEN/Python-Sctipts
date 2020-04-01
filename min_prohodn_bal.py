class Student():
    name = ""
    sumPoint = 0


# inFile = open("input.txt", 'r', encoding="utf8")
# outFile = open("output.txt", "w", encoding="utf8")
# lines = inFile.readlines()
# listOfLists = list()
# for line in lines:
#     myList = list(map(str, line.split()))
#     listOfLists.append(myList)
# listOfLists.sort(key=lambda x: x[0])
# for i in listOfLists:
#     print(i[0], i[1], i[3], file=outFile)
# inFile.close()
# outFile.close()


inFile = open("input.txt", 'r', encoding="utf8")
outFile = open("output.txt", "w", encoding="utf8")
k = int(inFile.readline())
lines = inFile.readlines()
listOfStudnts = list()
for line in lines:
    curLine = list(map(str, line.split()))
    point3 = int(curLine.pop())
    point2 = int(curLine.pop())
    point1 = int(curLine.pop())
    if point1 < 40 or point2 < 40 or point3 < 40:
        continue
    curStudent = Student()
    curStudent.name = " ".join(curLine)
    curStudent.sumPoint = point1 + point2 + point3
    listOfStudnts.append(curStudent)

listOfStudnts.sort(reverse=True, key=lambda x: x.sumPoint)
if len(listOfStudnts) > k:
    if k == 1:
        if listOfStudnts[0].sumPoint == listOfStudnts[1].sumPoint:
            print(1, file=outFile)
        else:
            print(listOfStudnts[0].sumPoint, file=outFile)
    elif k == 2:
        if listOfStudnts[1].sumPoint > listOfStudnts[2].sumPoint:
            print(listOfStudnts[1].sumPoint, file=outFile)
        elif listOfStudnts[1].sumPoint == listOfStudnts[2].sumPoint:
            if listOfStudnts[0].sumPoint == listOfStudnts[1].sumPoint:
                print(1, file=outFile)
            else:
                print(listOfStudnts[0].sumPoint, file=outFile)
    else:
        flag = 0
        lastStudent = listOfStudnts[k - 1]
        lastPoint = listOfStudnts[k - 1].sumPoint
        ls = listOfStudnts[k - 2]
        rs = listOfStudnts[k]
        if (ls.sumPoint > lastPoint) and (lastPoint == rs.sumPoint):
            lastStudent = listOfStudnts[k - 2]
        elif ls.sumPoint >= lastPoint > rs.sumPoint:
            lastStudent = listOfStudnts[k - 1]
        elif ls.sumPoint == lastPoint == rs.sumPoint:
            for i in range(k - 3, -1, -1):
                # print("in cycle")
                if listOfStudnts[i].sumPoint > lastPoint:
                    lastStudent = listOfStudnts[i]
                    break
                if i == 0:
                    flag = 1

        if flag == 1:
            print(1, file=outFile)
        else:
            print(lastStudent.sumPoint, file=outFile)
else:
    print(0, file=outFile)
inFile.close()
outFile.close()
