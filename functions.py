#3. Functions – Parameters, Default & Keyword Arguments
#3.1 What is a function?

#A function is a block of code that performs a specific task and can be reused.

#Syntax:
def function_name(parameters):
    # body
    return value   # optional

#3.2 Simple function and return

def add(a, b):
    s = a + b
    return s

result = add(3, 5)
print("Sum is:", result)

#Explanation:

#a and b are parameters.

#3 and 5 are arguments.

#return sends value back to the caller.

#3.3 Positional Arguments

#Arguments matched by position.

def power(base, exponent):
    return base ** exponent

print(power(2, 3))   # base = 2, exponent = 3 -> 8
print(power(3, 2))   # base = 3, exponent = 2 -> 9


#3.4 Default Arguments

#If value is not provided, default is used.

def greet(name, message="Welcome to Python!"):
    print(f"Hello {name}, {message}")

greet("Uday")                         # uses default message
greet("Lakshmi", "All the best!")     # custom message


#message="Welcome to Python!" is a default argument.


#3.5 Keyword Arguments

#We can specify arguments with name = value so order doesn’t matter.
def student_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

student_info(name="Uday", age=21, city="Hyderabad")

student_info(city="Delhi", name="Ankit", age=19)  # order changed


#3.6 Passing Lists & 2D Lists to Functions
#Function with list parameter

def find_max(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

arr = [3, 5, 2, 9, 1]
print("Maximum:", find_max(arr))


#Function with 2D list parameter

def print_matrix(mat):
    for row in mat:
        for val in row:
            print(val, end=" ")
        print()

m = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print_matrix(m)


################################################3.7 Combined Example (uses everything)

def read_marks(n_students):
    """Reads marks of n students and returns a list."""
    marks = []
    for i in range(n_students):
        mark = int(input(f"Enter marks of student {i+1}: "))
        marks.append(mark)
    return marks

def calc_average(marks):
    """Returns average of list of marks."""
    return sum(marks) / len(marks)

def classify_student(avg, pass_mark=35):
    """
    Returns PASS or FAIL based on avg.
    pass_mark has a default value 35.
    """
    if avg >= pass_mark:
        return "PASS"
    else:
        return "FAIL"

n = int(input("How many students? "))
marks_list = read_marks(n)
avg_marks = calc_average(marks_list)

print("Average marks:", avg_marks)
print("Result (pass_mark=35):", classify_student(avg_marks))
print("Result (pass_mark=40):", classify_student(avg_marks, pass_mark=40))
