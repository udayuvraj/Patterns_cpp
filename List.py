#Lists & Tuples
#Lists – Basics

#A list is an ordered collection of items. Lists are mutable (can be changed).

numbers = [10, 20, 30, 40]

print(numbers)       # [10, 20, 30, 40]
print(numbers[0])    # 10 (first element)
print(numbers[-1])   # 40 (last element)
print(numbers[1:3])  # [20, 30] (slice from index 1 to 2)


#Update elements:
numbers[1] = 25
print(numbers)       # [10, 25, 30, 40]

