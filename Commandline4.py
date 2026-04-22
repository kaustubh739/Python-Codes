import sys

def main():

    print("Number of arguments are : ",len(sys.argv))

    print("list of arguments are : ")

    for value in sys.argv:
        print(value)

if __name__ == "__main__":
    main()