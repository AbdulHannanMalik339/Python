my_dict = {}

my_dict = {1 : "Apple", 2 : "Banana", 3 : "Cherry"}

my_dict = {'name': 'Abdul' , 1 : [1, 2, 3, 4]}

my_dict = {'name' : 'Abdul' , 'age' : 14}

print(my_dict['name'])
print(my_dict['age'])

my_dict['age'] = 15
print(my_dict)

my_dict['address'] = '123 Main St'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address:", my_dict.get('address'))

my_dict.clear()
print(my_dict)