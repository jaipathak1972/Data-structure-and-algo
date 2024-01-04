# Find Second Smallest and Second Largest Element in an array
# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.

# def secondElement(arr: [], n: int) -> int:

#     if n == 0 or n == 1:
#         print(-1, -1)  # edge case when only one element is present in array
#     arr.sort()
#     small = arr[1]
#     large = arr[n-2]
#     print("Second smallest is", small)
#     print("Second largest is", large)



# number = secondElement([21,23,41,11,10,3,30],7)

# print(number)


# -------------------- optimal solution --------------------
def secondElement(arr: [], n: int) -> int:
    largest = 0
    secondlargest = -1
    for i in range(n):
        if arr[i] > largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i] > secondlargest and arr[i] != largest:
            secondlargest = arr[i]
    return secondlargest

number = secondElement([21, 23, 41, 11, 10, 3, 30], 7)
print(number) 


# Check if an Array is Sorted
# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check_sorting(arr: [], n: int) -> int:
    
    for i in range(n):
        if arr[i] <= arr[n+1]:
            return True,"ok"

        else:
            return False

number = check_sorting([1,2,2,3,3,4,5,6,7,8,9], 7)
print(number)