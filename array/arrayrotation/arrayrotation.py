#geeksforgeeks
#write a function rotate(arr[],d,n)that rotates arr[] of size n by d elements.
def rotate(arr,d,n):
    for i in range(d):
        leftrotate(arr,n)

def leftrotate(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

def printarray(arr,n):
    for i in range(n):
        print("%d"% arr[i],end=" ")

arr=[1,2,3,4,5,6,7,8]
rotate(arr,2,8)
printarray(arr,8)


        
