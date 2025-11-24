# Input and Output
#print() for output
print("Hello, World!")
print("Sum of 2 and 3 is", 2 + 3)

#input() for input
name = input("Enter your name: ")  # returns string
age = int(input("Enter your age: "))  # converted to int using int()

print("Hello", name)
print("Next year you will be", age + 1)

#f-strings (formatted strings)
marks = 95
print(f"{name} scored {marks} marks.")   # cleaner formatting