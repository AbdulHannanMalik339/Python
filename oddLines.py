file1 = open("file.txt", "r")
file2 = open("output.txt", "w")

cont = file1.readlines()
for i in range(len(cont)):
    if i % 2 == 0:
        file2.write(cont[i])

file2.close()

file2 = open("output.txt", "r")
cont1 = file2.read()

print(cont1)

file1.close()
file2.close()