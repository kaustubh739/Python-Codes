PI = 3.14 # code starts from this line memory allocation from this line but it will not be running

def main():
    print("Enter radius of circle")
    radius = float(input())

    Area = PI * radius * radius

    print("Area of circle is : ",Area)

if __name__ == "__main__":
    main()