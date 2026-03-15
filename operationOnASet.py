my_set ={1,2,3,4,5,6}
print("Set:", my_set)

my_set.add(7)
print("Set" , my_set)

set1 = my_set

set2 = {5,6,7,7,9}

print("\nSet 1:", set1)
print("Set 2:", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric_difference(set2))