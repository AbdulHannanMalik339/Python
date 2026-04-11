file = open('Me.txt', 'r')
print(file.read())
file.close()

file = open('Me.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Me.txt', 'w')
file.write("Hi my name is abdul hannan malik")
file.close()