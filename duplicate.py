outputFile = open("output.txt", "w")
inputFile = open("hi.txt" , "r")

lines_seen_so_far = set()
print("Eleminate duplicate lines")
for line in inputFile
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

outputFile.close()
inputFile.close()
