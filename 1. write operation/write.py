f = open("test.txt", "w")
f.write("Hasibur Rahman Green University of Bangladesh\n")
f.write("Department of CSE\n")

# write list of lines
lines = ["Hasibur ", "Ashikur ", "CGPA "]
f.writelines(lines)
f.close