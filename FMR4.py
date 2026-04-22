def increase(A):
    return A+1

def Demo(Task,Value):
    for x in Value:
        print(Task(x))

Data = [13,17,10,11,14]

Demo(increase, Data)