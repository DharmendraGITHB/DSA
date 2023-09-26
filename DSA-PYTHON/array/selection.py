def searchSort(arr):
	for i in range(len(arr)-1):
		min_val = i

		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_val]:
				min_val = j

		arr[i],arr[min_val] = arr[min_val],arr[i]

	return arr

def main():

	inputvalue= int(input("enter the input value you want: "))

	arr =[]
	for i in range(inputvalue):
		element = int(input(f"enter element {i+1}: "))
		arr.append(element)

	print("unsorted array:", arr)
	sort = searchSort(arr)

	print("sorted array:", sort)

if __name__ =="__main__":
	main()