# while loop

#Repeats as long as condition is True.

# print numbers from 1 to 5
i = 1                 # initialization
while i <= 5:         # condition
    print(i)
    i += 1            # update (i = i + 1)


#Things to remember:

#If you forget to update i, the loop may become infinite.

#Condition is checked before each iteration.

#for loop with range()

#range(start, stop, step) generates a sequence of numbers.

# print 1 to 5
for i in range(1, 6):   # 6 is excluded
    print(i)

# print 0 to 9
for i in range(10):     # default start = 0
    print(i, end=" ")

## Loop + Condition (example: sum of even numbers)
n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers from 1 to", n, "is", total)