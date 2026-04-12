import os
new_file = open('Me.txt', 'w')
new_file.close()

print("Checking if the file exists or not")
if os.path.exists("Me.txt"):
  os.remove("Me.txt")
else:
  print("The file does not exist")

my_file = open('Me.txt', 'w')
my_file.write("This is my file")
my_file.close()

os.remove("Me.txt")
os.rmdir("Hi")