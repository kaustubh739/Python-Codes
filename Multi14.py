import os
import time
import multiprocessing
def fun(no):
    print("PID is : ",os.getpid())
    sum = 0
    for i in range(1,no): # 1 to 9 no cube addition
        sum = sum + (i**3)
    return sum
    
def main():
    start_time = time.time()
    data = [10,20,30,40,50,60,70,80,90]
    #result = []
    
    p = multiprocessing.Pool()
    result = p.map(fun,data)

    p.close()
    p.join()

    print(result)

    end_time = time.time()

    print("execution time is : ",end_time - start_time)

if __name__ == "__main__":
    main()