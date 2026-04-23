PI = 3.14 # code starts from this line memory allocation from this line but it will not be running

def CircleArea(Rad):
    Area = PI * Rad * Rad
    return Area

def main():
    print("Enter radius of circle")
    radius = float(input())

    #Area = PI * radius * radius
    result = CircleArea(Rad = radius)

    print("Area of circle is : ",result)

if __name__ == "__main__":
    main()