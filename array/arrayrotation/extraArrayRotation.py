# Function to rotate arrays in Python

def RotateArrayLeft(arr, R, n):
    shift = []
    i = 0
    while (i < R):
        shift.append(arr[i])
        i = i + 1
    for i in range(n-R):
        arr[i] = arr[i+R]
    i = n-R
    j = 0
    while (i < n):
        arr[i] = shift[j]
        j += 1
        i = i + 1
    
    return arr

# Taking array input from user
n = int(input("how many element do you want in array: "))
arr = []
print("Enter elements of the array: ")
for i in range(n):
  numbers = int(input())
  arr.append(numbers)
R = int(input("Enter rotation count: "))

# printing array before rotation 
print("Initial Array: ", end = " ")
for i in range(n):
	print ("%d"% arr[i],end=" ")
	
RotateArrayLeft(arr, R, n)

# Printing array after rotation 
print("\nArray after rotation: ", end = " ")
for i in range(n):
	print ("%d"% arr[i],end=" ")
