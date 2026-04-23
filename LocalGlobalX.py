no = 11

def fun():
    global no
    print("inside fun")
    x = 21
    print("value of x is : ",x) # 21
    print("value of no : ",no) # 11
    no = no + 1
    print("value of no : ",no)

def main():
    print("value of no before fun : ",no)
    fun()
    print("value of no before fun : ",no)

if __name__ == "__main__":
    main()