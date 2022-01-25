#geeksforgeeks
#program for linear search finding x elements location in arr[]

def linearsearch(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return 'element is not present in array'


arr=[1,2,3,4,5]
n=len(arr)
x=4
#call the function
find=linearsearch(arr,n,x)
print('x:',find)
