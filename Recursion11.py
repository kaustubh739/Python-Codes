# Input : 4
# output : 10 (4+3+2+1)
# every loops will convert into recursion
sum = 0

def Add(no):
    global sum
    
    if (no >= 1):
        sum = sum + no
        no = no - 1
        Add(no)
    return sum

def main():
    ret = Add(4)
    print("solution is : ",ret)
    #print(sum)

if __name__ == "__main__":
    main()