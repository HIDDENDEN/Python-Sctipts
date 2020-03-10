p, x, y = int(input()), int(input()), int(input())
multP = (100 + p) / 100
sum = 0.0
sum = x + y * 0.01
sum *= multP
ost = sum - int(sum)
ost += 0.000001
# print(ost)
# print(int(ost * 100))
print(int(sum), int(ost * 100), sep=" ")
