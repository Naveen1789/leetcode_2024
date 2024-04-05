'''
Bubble Sort: Given an unsorted array, sort it in ascending order.

    Pseudo code:
        for i in range of 0 to len(arr)-1:
            for j in range of 0 to len(arr) - i - 1:
                if (arr[j] > arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

    Time complexity: O(n^2)

    Space complexity: O(1)
'''

def bubble_sort(arr):
    print ("Sorting " + str(arr) + "...")
    for i in range(0,len(arr)-1):
        for j in range (0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print ("Sorted array: " + str(arr))

arr1 = [1, 17, 5, -10, 25, 21]
bubble_sort(arr1)
