#1.Selection Sort

#For each position i in array:

#Assume arr[i] is smallest.

#Scan remaining part to find actual smallest element.

#Swap that smallest element with arr[i].

#Time complexity: O(n²).


# SELECTION SORT

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume current index i has the minimum
        min_idx = i

        # Find index of smallest element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap if smaller element found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# --- Input & Output ---
size = int(input("Enter number of elements: "))
nums = []
for _ in range(size):
    nums.append(int(input()))

print("Original array:", nums)
sorted_nums = selection_sort(nums)
print("Sorted array (Selection Sort):", sorted_nums)




#7️.Insertion Sort

#Maintain a sorted part on the left.

#Take each element (key), and insert it into correct position in the sorted part (like arranging cards).

#Time complexity: O(n²), good for nearly sorted arrays.


# INSERTION SORT

def insertion_sort(arr):
    n = len(arr)
    # Start from index 1 (0th element is trivially sorted)
    for i in range(1, n):
        key = arr[i]      # element to insert
        j = i - 1

        # shift elements greater than key one step to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key in its correct position
        arr[j + 1] = key

    return arr


# --- Input & Output ---
size = int(input("Enter number of elements: "))
nums = []
for _ in range(size):
    nums.append(int(input()))

print("Original array:", nums)
sorted_nums = insertion_sort(nums)
print("Sorted array (Insertion Sort):", sorted_nums)



#3.Bubble Sort

#Compare adjacent elements and swap if they’re in wrong order.

#After 1 full pass, largest element goes to the end.

#Repeat for remaining part.
#Time: O(n²), Space: O(1).

# BUBBLE SORT IMPLEMENTATION

def bubble_sort(arr):
    n = len(arr)

    # Outer loop for passes
    for i in range(n):
        # Flag to detect if any swap happened in this pass
        swapped = False

        # Last i elements are already in correct position
        for j in range(0, n - 1 - i):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Optimization: if no swap happened, array already sorted
        if not swapped:
            break

    return arr


# --- INPUT + OUTPUT EXAMPLE ---
size = int(input("Enter number of elements (Bubble sort): "))
nums = []
for _ in range(size):
    nums.append(int(input()))

print("Original:", nums)
print("Sorted using Bubble Sort:", bubble_sort(nums))




#4.Merge Sort
#Divide and Conquer

#Steps:

#Divide array into 2 halves recursively.
S#ort each half.
#Merge two sorted halves into one sorted array.
#Time: O(n log n), Space: O(n)


# MERGE SORT IMPLEMENTATION

def merge(left, right):
    """
    Merge two sorted lists (left and right)
    into a single sorted list.
    """
    i = j = 0
    result = []

    # Take smallest from left or right and append
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    # Base case: 0 or 1 element -> already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Recursively sort left and right halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge two sorted halves
    return merge(left_half, right_half)


# --- INPUT + OUTPUT EXAMPLE ---
size = int(input("Enter number of elements (Merge sort): "))
nums = []
for _ in range(size):
    nums.append(int(input()))

print("Original:", nums)
print("Sorted using Merge Sort:", merge_sort(nums))


#5. Quick Sort

#Also divide and conquer.
#Pick a pivot element.
#Partition array so:
#elements < pivot on left
#elements > pivot on right
#Recursively quicksort left and right part.

#Average time: O(n log n), worst case: O(n²) (if pivot bad).
#Space: O(log n) (recursion stack).

#Code (Lomuto partition, in-place)

# QUICK SORT IMPLEMENTATION (IN-PLACE)

def partition(arr, low, high):
    """
    Lomuto partition:
    - Pick last element as pivot
    - Place pivot at correct position
    - Elements <= pivot on left, > pivot on right
    """
    pivot = arr[high]
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot after smaller elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # pi is partition index
        pi = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# --- INPUT + OUTPUT EXAMPLE ---
size = int(input("Enter number of elements (Quick sort): "))
nums = []
for _ in range(size):
    nums.append(int(input()))

print("Original:", nums)
quick_sort(nums, 0, len(nums) - 1)
print("Sorted using Quick Sort:", nums)



#6. Counting Sort
#Works for non-negative integers in a known small range (e.g., 0–1000).

#Idea:

#Count frequency of each value.

#Use counts to place elements in correct position.

#Time: O(n + k) where k is range (max value).
#Space: O(k).

#Don’t use this for large values (like up to 10⁹); memory will explode.


# COUNTING SORT IMPLEMENTATION
# Assumption: all numbers are >= 0

def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)  # highest number in array

    # count array of size max_val+1 initialised with 0
    count = [0] * (max_val + 1)

    # 1) Store the count of each element
    for num in arr:
        count[num] += 1

    # 2) Build the sorted array using the counts
    index = 0
    for value in range(max_val + 1):
        # repeat 'value' count[value] times
        while count[value] > 0:
            arr[index] = value
            index += 1
            count[value] -= 1

    return arr


# --- INPUT + OUTPUT EXAMPLE ---
size = int(input("Enter number of elements (Counting sort): "))
nums = []
for _ in range(size):
    nums.append(int(input()))

print("Original:", nums)
print("Sorted using Counting Sort:", counting_sort(nums))


#8. #Using sorted() and list.sort() for Optimization

#Python gives highly optimized Timsort internally for these.

############sorted(iterable)
#it will returns new sorted list
#wit orks on any iterable (list, tuple, string…)

#######list.sort()
#it will sorts the list in-place
#returns None

#Both have average time O(n log n) and are much faster than writing Bubble/Insertion etc in Python.
#Basic usage of this:

# USING sorted() AND list.sort()

nums = [5, 3, 8, 1, 2]

# 1) sorted() -> does NOT modify original list
sorted_nums = sorted(nums)        # ascending order
print("Original:", nums)
print("sorted(nums):", sorted_nums)

# 2) sorted() with reverse=True
print("sorted(nums, reverse=True):", sorted(nums, reverse=True))

# 3) list.sort() -> sorts in-place
nums.sort()                       # ascending
print("After nums.sort():", nums)

# 4) list.sort(reverse=True)
nums.sort(reverse=True)
print("After nums.sort(reverse=True):", nums)
