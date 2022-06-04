#geeksforgeeks
""" note- a binary search or half-interval algorithm is work on sorted arrays. """
#given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

def binarysearch(arr,x,low,high):
    if low <= high:
        mid = low + (high -low)//2
                                             #x is array elements
                                             #low, high are the index value.


