# Tuple

# Syntax : ()
# Heterogeneous
# ordered
# index
# data immutable
# tuple immutable
# duplicate
# 
data = (10,"Hello",90.67, True,10)
print("data type is : ",type(data))
print("length is : ",len(data))
print(data)
print(data[0])
print(data[1])

data[0] = 11

print("data using loop")
for value in data:
    print(value)

print("data using index")
for i in range(len(data)):
    print(data[i])
