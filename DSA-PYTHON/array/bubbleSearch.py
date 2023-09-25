#bubble sort algorithm

def bubble_sort(arr):
	for i in range(len(arr)-1):  
		for j in range(len(arr)-i-1): 
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1], arr[j]

	return arr

def main():

	
	user_input = int(input("enter the number of input YOU WANT: "))

	arr = []
	for i in range(user_input):
		element = input(f"enter a element {i+1}: ")
		arr.append(element)

	print('sorted array', bubble_sort(arr))

if  __name__ == "__main__":
	main()