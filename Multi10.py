import multiprocessing
import time
import os
def SumEven(no):
    print("PID of sumeven process is ",os.getpid())
    print("PPID of sumeven process is ",os.getppid())

    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    print (sum)

def SumOdd(no):
    print("PID of sumeodd process is ",os.getpid())
    print("PPID of sumodd process is ",os.getppid())

    sum = 0
    for i in range(1,no+1,2):
        sum = sum + i
    print(sum)
    
def main():
    print("Demonstration of parallel execution")
    print("PID of sumeodd process is ",os.getpid())

    start_time = time.time()

    P1 = multiprocessing.Process(target=SumEven,args=(900000000,))
    P2 = multiprocessing.Process(target=SumOdd,args=(900000000,))

    P1.start()
    P2.start()

    P1.join()
    P2.join()

    end_time = time.time()

    print("Time required for execution is : ",end_time - start_time)
    print("end of main")


if __name__ == "__main__":
    main()