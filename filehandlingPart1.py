with open('hi.txt', 'w') as file:
    file.write("Hello World")
    file.close()

with open('hi.txt', 'r') as file:
    data =  file.readlines()
    print("Words in the file are ")
    for line in data:
        word = line.split()
        print(word)
    file.close()