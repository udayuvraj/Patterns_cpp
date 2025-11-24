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



