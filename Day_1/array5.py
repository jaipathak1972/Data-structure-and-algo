# Left Rotate the Array by One
# Problem Statement: Given an array of N integers, left rotate the array by one place.
def rotate_array(arr: [], n: int) -> []:
    temp = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]  # Shift elements to the right
    
    arr[0] = temp  # Set the first element to the last

    return arr

number = rotate_array([1,2,2,3,3,4,5,6,7,8,9], 7)
print(number)



