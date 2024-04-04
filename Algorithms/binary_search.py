'''
Binary Search: Given a sorted array and a target, find if the target exists in the array. If it does, return the index of the target within the array. If not, return -1.
[Assume the array doesn't have any duplicates.]

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
