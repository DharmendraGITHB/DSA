
#method for cyclically rotation of given array by one

def rotate(arr,n):
    x=arr[n-1]

    for i in range(n-1, 0, -1):
        arr[i]=arr[i-1]

    arr[0]=x

arr=[1,2,3,4,5,6]
n=len(arr)
print("Input array")
print(arr)

rotate(arr,n)
print("Rotated array:")
print(arr)



