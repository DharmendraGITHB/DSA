# binary search

#recursive method to solve the binary search

def recurbinary(arr, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
  
  # if element found in the middle of array then simply return to function
        if arr[mid]==x:
            return mid
  # in this situation search the left half using recursion method33 
        elif arr[mid] > x:
            return recurbinary(arr, x, low, mid-1)

        else:
            return recurbinary(arr, x, mid+1, high)


    else:
        return -1


arr = [1,2,3,4,5,6,7,8,9,10]

x= 6

result = recurbinary(arr, x, 0,9)

if result != -1:
    print("element is exist at index: ", result)

else:
    print("not exist")

        
