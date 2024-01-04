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