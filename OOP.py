class Arithematic:

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Result = 0
        Result = self.No1 + self.No2
        return Result
def main():

    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    obj = Arithematic(value1,value2)
    Ret = obj.Addition()

    print("addition is : ",Ret)


if __name__ == "__main__":
    main()