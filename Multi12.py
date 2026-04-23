import os

def fun(no):
    sum = 0
    for i in range(1,no): # 1 to 9 no cube addition
        sum = sum + (i**3)
    return sum
    
def main():
    ret = fun(9)
    print(ret)

if __name__ == "__main__":
    main()