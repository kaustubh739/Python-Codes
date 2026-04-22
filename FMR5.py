def increase(A):
    return A+1

def Demo(Task,Value):
    Result = []

    for no in Value:
        ret = Task(no)
        Result.append(ret)
    return Result

Data = [13,17,10,11,14]

Rdata = list(Demo(increase, Data))
print(Rdata)