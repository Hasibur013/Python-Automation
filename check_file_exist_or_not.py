import os.path

if os.path.isfile("test.txt"):
    print("test.txt file exist")
else:
    print("test.txt file doesn't exist")
    
# Example: read file with checking 

filename = "test.txt"

if os.path.isfile(filename):
    with open(filename , "rt") as f:
        data = f.read()
        print(data)
else:
    print(" file doesn't exist")