file_read = open('Me.txt', 'r')
print("File in read mode")
print(file_read.read())
file_read.close()

file_write = open('Me.txt', 'w')
print("File in write mode")
file_write.write("Hi my name is abdul hannan malik")
file_write.close()

file_append = open('Me.txt', 'a')
print("\n File in append mode")
file_append.write("\n I am a student of computer science")
file_append.close()