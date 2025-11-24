#1️. String Manipulation
#A string = sequence of characters.

#Common operations:

#Length (len)
#Indexing & slicing (s[i], s[a:b])
#Changing case (upper, lower, title)
#Search (find, in)
#Replace (replace)
#Split & join (split, join)

# STRING MANIPULATION EXAMPLES

text = "Hello World"

# 1. Length of the string
print("Original string:", text)
print("Length:", len(text))  # counts characters including space

# 2. Indexing
print("First character:", text[0])    # 'H'
print("Last character:", text[-1])    # 'd'

# 3. Slicing (substring)
print("First 5 characters:", text[0:5])   # 'Hello'
print("From index 6 to end:", text[6:])   # 'World'

# 4. Reverse a string using slicing
print("Reversed string:", text[::-1])

# 5. Changing case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# 6. Searching in a string
print("'World' in text?", "World" in text)    # True / False
print("Index of 'World':", text.find("World"))  # returns starting index or -1

# 7. Replacing
print("Replace 'World' with 'Python':", text.replace("World", "Python"))

# 8. split() -> string to list | join() -> list to string
words = text.split(" ")   # split at space
print("Split into words:", words)

joined_with_dash = "-".join(words)    # join using "-"
print("Joined with dash:", joined_with_dash)




#2️. Palindrome (String + Number)

#A palindrome reads the same forwards and backwards.

#Examples: "madam", "racecar", 121, 12321.

#We compare the string with its reverse.

##################################string palindrome

# PALINDROME CHECK FOR STRING

def is_palindrome_string(s: str) -> bool:
    # Convert to lowercase
    s = s.lower()
    # Remove spaces (so "nurses run" also works)
    s = s.replace(" ", "")
    # Check if string equals its reverse
    return s == s[::-1]


# --- Input from user and output ---
user_str = input("Enter a string to check palindrome: ")
if is_palindrome_string(user_str):
    print("It is a palindrome.")
else:
    print("It is NOT a palindrome.")



############################################# Number Palindrome


# PALINDROME CHECK FOR NUMBER

def is_palindrome_number(n: int) -> bool:
    # Convert number to string and compare with its reverse
    s = str(n)
    return s == s[::-1]


num = int(input("Enter a number to check palindrome: "))
if is_palindrome_number(num):
    print("Number is a palindrome.")
else:
    print("Number is NOT a palindrome.")




#3️. Anagram

#Two strings are anagrams if:
#They have the same characters with same frequency.
#Order doesn’t matter.
#Example: "listen" and "silent".

#Method 1: Sort and Compare


# ANAGRAM CHECK USING SORTING

def are_anagrams(s1: str, s2: str) -> bool:
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Sort characters and compare
    return sorted(s1) == sorted(s2)


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if are_anagrams(str1, str2):
    print("They are anagrams.")
else:
    print("They are NOT anagrams.")



#4️. Matrix Traversals (Row-wise, Column-wise, Diagonals)

#We’ll use a 2D list to represent a matrix.
# MATRIX TRAVERSALS

# Sample 3x3 matrix
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(mat)
cols = len(mat[0])

print("Matrix:")
for row in mat:
    print(row)

# 1) Row-wise traversal (normal reading: row by row)
print("\nRow-wise traversal:")
for i in range(rows):        # for each row
    for j in range(cols):    # for each column in that row
        print(mat[i][j], end=" ")
    print()                  # new line after each row

# 2) Column-wise traversal
print("\nColumn-wise traversal:")
for j in range(cols):        # fix column
    for i in range(rows):    # move through rows
        print(mat[i][j], end=" ")
    print()

# 3) Main (primary) diagonal: (0,0), (1,1), (2,2), ...
print("\nMain diagonal:")
for i in range(rows):
    print(mat[i][i], end=" ")
print()

# 4) Secondary diagonal: (0,n-1), (1,n-2), ...
print("\nSecondary diagonal:")
for i in range(rows):
    j = cols - 1 - i   # column index from right side
    print(mat[i][j], end=" ")
print()


#5️. Diagonal Sum (Primary + Secondary)
# DIAGONAL SUMS IN A SQUARE MATRIX

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(mat)  # n x n square matrix

primary_sum = 0
secondary_sum = 0

for i in range(n):
    primary_sum += mat[i][i]           # primary diagonal element
    secondary_sum += mat[i][n - 1 - i] # secondary diagonal element

print("Primary diagonal sum:", primary_sum)
print("Secondary diagonal sum:", secondary_sum)

# If we want total of both diagonals counting center only once:
if n % 2 == 1:
    # center element counted twice; subtract once
    center = mat[n // 2][n // 2]
    total_diagonal_sum = primary_sum + secondary_sum - center
else:
    total_diagonal_sum = primary_sum + secondary_sum

print("Total diagonal sum (center counted once):", total_diagonal_sum)


