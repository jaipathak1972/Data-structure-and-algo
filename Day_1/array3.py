# Check if an Array is Sorted
# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check_sorting(arr: [], n: int) -> bool:
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

list1 = check_sorting([1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9], 11)
list2 = check_sorting([1, 2, 2, 3, 4, 3, 4, 5, 6, 7, 8, 9], 12)
print(list1)
print(list2)

