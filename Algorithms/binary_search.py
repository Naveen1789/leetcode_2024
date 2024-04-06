'''
Binary Search: Given a sorted array and a target, find if the target exists in the array. If it does, return the index of the target within the array. If not, return -1.
[Assume the array doesn't have any duplicates.]

    Algorithm:
        Step 1 − Select the middle item in the array and compare it with the key value to be searched. If it is matched, return the position of the median.
        Step 2 − If it does not match the key value, check if the key value is either greater than or less than the median value.
        Step 3 − If the key is greater, perform the search in the right sub-array; but if the key is lower than the median value, perform the search in the left sub-array.
        Step 4 − Repeat Steps 1, 2 and 3 iteratively, until the size of sub-array becomes 1.
        Step 5 − If the key value does not exist in the array, then the algorithm returns an unsuccessful search.

    Pseudo code:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) / 2
            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    Time complexity: O(log n)

    Space complexity: O(1)

    NOTE: THE BELOW TWO LINES ARE THE SAME
    - mid = low + ((high - low) / 2)
    - mid = (low + high) / 2

    [EXCEPT, SOMETIMES (low + high) MIGHT PRODUCE INTEGER OVERFLOW]
'''

def binary_search(arr, target):
    print ("Searching for " + str(target) + " in " + str(arr) + "...")
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) / 2
        if target == arr[mid]:
            print ("====> Target found at index " + str(mid) + ".")
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print ("====> Target not found in the array.")
    return -1

arr1 = [-10, 1, 5, 17, 21, 25]

# targets_arr1 = [-10, 1, 5, 17, 21, 25, 49]
# for t in targets_arr1:
#     binary_search(arr1, t)

arr2 = [-100, -10, 1, 5, 17, 21, 25]
targets_arr2 = [-100, -10, 1, 5, 17, 21, 25, 49]
for t in targets_arr2:
    binary_search(arr2, t)
