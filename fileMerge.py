with open ('hi.txt', 'r') as fp:
    data1 = fp.read()

with open ('file.txt', 'r') as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files")
with open ('output.txt', 'w') as fp:
    fp.write(data1)