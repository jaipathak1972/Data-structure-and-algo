# # Move all Zeros to the end of the array
# In this article we will learn how to solve the most asked coding interview problem: “Move all Zeros to the end of the array”

# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.


# ---------------------------------------------optimal soltion ---------------------------------------
def moveZeros(n: int,  a: [int]) -> [int]:
    j = -1
    # Place the pointer j
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    
   
    if j == -1:
        return a
    
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    
    return a


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=' ')
print()