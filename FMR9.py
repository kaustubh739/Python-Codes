from MarvellousFMR import filterX, mapX, reduceX  # type: ignore

CheckEven = lambda No : (No%2 == 0)
Increase = lambda No: No+1
Sum = lambda A,B : A+B


#import MarvellousFMR
def main():
    Data = []

    print("Enter number of elements : ")
    size = int(input())

    print("please enter numeric values : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input data : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Filter output : ",FData)

    MData = list(mapX(Increase,FData))
    print("map output : ",MData)

    RData = reduceX(Sum,MData)
    print("reduce output : ",RData)

if __name__ == "__main__":
    main()
