no = 11

def fun():
    print("inside fun")
    x = 21
    print("value of x is : ",x) # 21
    print("value of no : ",no) # 11

def sun():
    print("inside sun")
    y = 51
    print("value of y is : ",y) # 51
    print("value of no : ",no) # 11

def main():
    fun()
    sun()

if __name__ == "__main__":
    main()