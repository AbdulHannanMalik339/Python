file_read = open("file.txt", "r")
print("File in read mode:")
print(file_read.read())
file_read.close()

file_write = open("file.txt", "w")
file_write.write("File in write mode....")
file_write.write("Hello i am hannan i am 14 years old")
file_write.close()