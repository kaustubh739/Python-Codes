from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

increase = lambda No : No + 1
    

Sum = lambda A,B : A+B


Data = [7,10,15,12,4,6,9,8,12,16]
print("Input Data : ",Data)

FData = list(filter(CheckEven, Data))
print("Filter Output : ",FData)

MData = list(map(increase, FData))
print("Map Output : ",MData)

RData = reduce(Sum, MData)
print("Reduce Output : ",RData)