'''
Bubble Sort: Given an unsorted array, sort it in ascending order.

    Algorithm:
        Step 1 − Check if the first element in the input array is greater than the next element in the array.
        Step 2 − If it is greater, swap the two elements; otherwise move the pointer forward in the array.
        Step 3 − Repeat Step 2 until we reach the end of the array.
        Step 4 − Check if the elements are sorted; if not, repeat the same process (Step 1 to Step 3) from the last element of the array to the first.
        Step 5 − The final output achieved is the sorted array.
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
