import sys
def main():
    print("Number of commandline arguments are : ",len(sys.argv))
    print("First command line argument is : ",sys.argv[0])
    print("datatype of argv is : ",type(sys.argv))
    print("second command line argument is : ",sys.argv[1])
    print("third command line argument is : ",sys.argv[2])
    print("fourth command line argument is : ",sys.argv[3])


if __name__ == "__main__":
    main()