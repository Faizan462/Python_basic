f = open("file_handling_practice.txt", "r")

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1)
print(line2)
print(line3)

# lines = f.readlines()
# for line in lines:
#     print(line) 

f.close()

f = open("file_handling_practice.txt", "a")

f.write("This is the new line added to the file.\n")
f.write("This is another new line added to the file.\n")

f.close()