# Find the Largest element in an array
# Problem Statement: Given an array, we have to find the largest element in the array.

# ------------------- BRUTE SOLUTION --------------
def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    arr.sort(reverse=False)


    return arr[-1]



number = largestElement([21,23,41,11,10,3,30],7)

# print(number);

# ---------------optiman solution ----------------~

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    j = -1
    for i in range(n):
        if j < arr[i]:
            j = arr[i]


    return j



number = largestElement([21,23,41,11,10,3,30],7)

print(number)
