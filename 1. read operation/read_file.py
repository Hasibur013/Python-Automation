f = open("test.txt", "r")

print(f.read())

print(f.readline())

for x in f:
  print(x)

f.close()

