# Linear Search  in python 
# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

def search(arr, n, num):
    for i in range(n):
        if arr[i] == num:
            return i
    return -1

# Test Case
arr = [1, 2, 3, 4, 5]
num = 4
n = len(arr)
val = search(arr, n, num)
print(val)
