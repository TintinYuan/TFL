# Created by Dingran Yuan
def quickSort(arr):
    '''
    Perform the quick sort to a list of numbers

    arr -- an unsorted input list
    '''
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)