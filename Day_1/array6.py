# ----------------------------------optimal solution ---------------------------------------
def rotate_to_right(arr, n, k):
    if n == 0:
        return
    k = k % n
    if k > n:
        return
    temp = arr[n - k:]
    for i in range(n - k - 1, -1, -1):
        arr[i + k] = arr[i]
    for i in range(k):
        arr[i] = temp[i]

# Test Case
n = 7
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotate_to_right(arr, n, k)

print("After Rotating the elements to right:")
for i in range(n):
    print(arr[i], end=" ")
