# Set

# syntax : {}
# heterogenous
# unordered
# unindexed
# duplicate not allowed
# Set is mutuable
# data is immutable

data = {10,"Hello",90.67,True,10}
print("datatype is :", type(data))
print("length is : ",len(data))
print(data)
#print(data[0])

#data[0] = 11
#print (data[0])

data.add(71)
print(data)

data.remove(10)
print(data)

print("data using loop")
for value in data:
    print(value)