'''
Linear Search (Sequential Search): Given an unsorted array and a target, find if the target exists in the array. If it does, return the index of the target within the array. If not, return -1.
[Assume the array doesn't have any duplicates.]

    Pseudo code:
        i = 0
        while i < len(arr):
            if arr[i] == target:
                return i
            i = i+1
        return -1

    Time complexity: O(n)

    Space complexity: O(1)
'''

def linear_search(arr, target):
    print ("Searching for " + str(target) + "...")
    i = 0
    while i < len(arr):
        if arr[i] == target:
            print ("Target found at index " + str(i) + ".")
            return i
        i = i+1
    print ("Target now found in the array.")
    return -1

arr1 = [1, 17, 5, -10, 25, 21]
target1 = 17
target2 = 22
linear_search(arr1, target1)
linear_search(arr1, target2)
