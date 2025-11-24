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


#2.2 Common List Operations
nums = [1, 2, 3]

nums.append(4)           # add 4 at the end
# nums -> [1, 2, 3, 4]

nums.insert(1, 10)       # insert 10 at index 1
# nums -> [1, 10, 2, 3, 4]

nums.extend([5, 6])      # extend by another list
# nums -> [1, 10, 2, 3, 4, 5, 6]

print(nums)

nums.remove(10)          # remove first occurrence of 10
last = nums.pop()        # remove last element and return it

print("Popped:", last)
print("List now:", nums)

print("Length:", len(nums))
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))


#Loop through list and compute average

marks = [80, 90, 75, 88]

total = 0
for m in marks:
    total += m

avg = total / len(marks)
print("Average marks:", avg)

