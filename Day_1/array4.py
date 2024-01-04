# Remove Duplicates in-place from Sorted Array
# Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.


def unique_list(arr: [], n: int) -> bool:
    
    
    j= 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return arr, j+1
 





list1 = unique_list([1, 2, 2, 8, 8], 5)
print(list1)

