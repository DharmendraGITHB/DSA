#reverse array algorithm

def reverserotation(arr,start,end):
    while (start < end):

        first=arr[start]
        
        arr[start]=arr[end]
        
        arr[end]=first
        
        start += 1
        
        end -= 1



def leftrotate(arr,n,d):

    if d==0:
        
        return
    
    #if d is greater than n
    
    d=d%n

    reverserotation(arr,0,d-1)   #reverse first part of array Ar

    reverserotation(arr,d,n-1)   #reverse second part of array ArBr
    
    reverserotation(arr,0,n-1)   #reverse complete array BrAr


def printreverse(arr):
    
    for i in range(len(arr)):
    
        print(arr[i], end=" ")

arr=[1,2,3,4,5,6,7,8,9]

d=3                              #rotate by d elements

n=len(arr)

leftrotate(arr,n,d)

printreverse(arr)
