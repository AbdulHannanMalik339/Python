list = ["Apple", "Banana", "Cherry"]

print("Length of the list:", len(list))
print("First item:", list[0])
print("Last item:", list[-1])

list.append("Orange")
print("List after appending:", list)

list.sort()
print("List after sorting:", list)

list.pop()
print("List after popping:", list)

list.reverse()
print("List after reversing:", list)

print("Multiplication on list:", list * 2)

list=  list[:2]
print("List after slicing:", list)

list.clear()
print("List after clearing:", list)