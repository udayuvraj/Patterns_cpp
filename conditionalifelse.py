#Conditionals (if / elif / else)

#Used to perform different actions based on conditions.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


#Explanation:

#if condition is checked first.

#If false, then elif conditions checked (if present).

#If all fail, else block executes.

#Example: Check whether a number is even or odd.

n = int(input("Enter n: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


#n % 2 gives remainder when divided by 2.
#If remainder is 0 → even, else → odd.