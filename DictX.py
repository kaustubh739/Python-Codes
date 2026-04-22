

data = {"Name" : "Let us C", "Author" : "Y Kanetkar", "price" : 340, "Publication" : "BPB Publication"}

print("Loop to display keys")
for X in data:
    print(X)

print("loop to display value")
for X in data.values():
    print(X)

print("loop to display key and value")
for X, Y in data.items():
    print(X,Y)