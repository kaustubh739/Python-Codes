# Dict

# syntax : {key : value}
# Heterogeneous
# ordered
# index (not numeric)
# key duplicate allowed but old gets overwritten
# value duplicate allowed
# data mutable (value)

data = {"Name" : "Let us C", "Author" : "Y Kanetkar", "price" : 340, "Publication" : "BPB Publication"}
print("datatype is ", type(data))
print("length is : ",len(data))
print(data)

print(data["Author"])

data["price"] = 400
print(data)