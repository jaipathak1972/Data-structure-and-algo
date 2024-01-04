# ---------------------- brute solution ----------------------
def missing_number(a, N):
    # Outer loop that runs from 1 to N:
    for i in range(1, N + 1):
        # flag variable to check if an element exists
        flag = 0

        # Search the element using linear search:
        for j in range(len(a)):
            if a[j] == i:
                # i is present in the array:
                flag = 1
                break

        if flag == 0:
            return i
    return -1

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missing_number(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()
# -------------------------------- optimal solution -----------------------------------------
    


def missingNumber(a, N):

    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(a)

    missingNum = summation - s2
    return missingNum

def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()

