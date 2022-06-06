# binary search problem
# Ascending order
# iterative method
# binary search should be sorted first

def binarysearch(arr, x, low, high):
    while low<=high:

        mid = low + (high-low)//2


        if arr[mid]==x:
            return mid
        
        elif arr[mid]<x:
            
            low = mid + 1

        else:
            high = mid - 1


    return -1

arr = [1,2,3,4,5,6,7,8,9,10]

x= 6

result = binarysearch(arr, x, 0, 9)

if result != -1:
    print("element is present" )
else:
    print("not found")
