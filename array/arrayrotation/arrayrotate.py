#juggling algorithm
#number of set is equal to gcd(d,n),move the elements within sets.
#sets are {1,2,3},{4,5,7}

#Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

def rotate(arr,d,n):
    for i in range(gcd(d,n)):  #call to def gcd(a,b)
        temp=arr[i]            #i is index and arr[i],arr[k] & arr[j] is element/data of same array.
        j=i                    #initial iteration i=0,arr[0]=1 in array
        while 1:               #while 1 is the same as while True.It means loop forever.
            k=j+d
            if k>=n:
                k-=n           #k=k-n
            if k==i:
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp

def gcd(a,b):  #b=n=7, a=d=2 #return value gcd(a,b)=2
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def printarray(arr, size):
    for i in range(size):
        print("%d"%arr[i], end=' ')

#gcd =greatest commom divisor
d=2
arr=[1,2,3,4,5,6]
n=len(arr)
d=d%n     #The quotient and remainder of 2 divided by 7=0R2,also known as Euclidean division

#call the function
rotate(arr,d ,n)
printarray(arr,n)
