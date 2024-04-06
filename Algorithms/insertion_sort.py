'''
Insertion sort:
    Algorithm:
        Step 1 - If the element is the first element, assume that it is already sorted. Return.
        Step 2 - Pick the next element, and store it separately in a key.
        Step 3 - Now, compare this key with all elements in the sorted array (left).
        Step 4 - If the element in the sorted array is smaller than the key element, then break and move to the next iteration.
                 Else, shift greater elements in the array towards the right.
                 Insert the key element.
        Step 5 - Repeat until the array is sorted.

    Pseudo code:
        i = 1

        while i in range of 1 to len(arr):
            key = arr[i]
            j = i - 1
            while (j > -1) and (arr[j] >= key):
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = key

    Time complexity: O(n^2)

    Space complexity: O(1)
'''

def insertion_sort(arr):
    print ("Sorting " + str(arr) + "...")
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while ((j > -1) and (arr[j] >= key)):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    print ("Sorted array: " + str(arr))

arr1 = [1, 17, 5, -10, 25, 21]
insertion_sort(arr1)
