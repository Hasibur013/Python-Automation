f = open("E:\python\Python Automation/test.txt", "r")

print(f.read())

print(f.readline())

for x in f:
  print(x)

f.close()

