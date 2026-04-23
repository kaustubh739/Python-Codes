def CalculatePercentage(Total, Obtained):
    output = ((Obtained/Total)*100)
    return output


def main():
    print("Enter total marks : ")
    Value1 = int(input())

    print("Enter Obtained marks : ")
    Value2 = int(input())

    #output = ((Value2/Value1)*100)
    result = CalculatePercentage(Value1, Value2) # Positional Argument


    print("Prcentage is : ",result)

if __name__ == "__main__":
    main()
