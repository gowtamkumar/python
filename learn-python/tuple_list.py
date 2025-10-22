# list operations
list_data = [5, 2, 9, 1, 5, 6, 33, 44, 23]
print("Original list:", list_data)

# print("Tuple from list:", list_data[0])
list_data.append(99)
list_data.sort()
print(list_data)

list_data.sort(reverse=True)

print(list_data)

# The sorted() function returns a new sorted list, leaving the original list unchanged
print("Using sorted():", sorted(list_data, reverse=True))
list_data.reverse()
list_data.insert(2, 111)
list_data.remove(2)
list_data.pop()
list_data.pop(6)
print(list_data)

# tuple operations
tuple_data = (
    5,
    2,
    9,
    1,
    5,
    6,
    33,
    44,
    23,
)
print(tuple_data.index(33))
print(tuple_data.count(5))

print("Original tuple:", tuple_data)
