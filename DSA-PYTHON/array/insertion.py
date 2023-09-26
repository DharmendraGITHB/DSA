
def Insertion(arr):
	n= len(arr)
	for i in range(1, n):
		current_element= arr[i]          #started from the second element
		j = i-1                 # here we storing indices 

		while j>=0 and arr[j] > current_element:
			arr[j+1] = arr[j]

			j -=1      #In ist iteration it become j= -1 because j is already zero here

		arr[j+1] = current_element

	return arr



def main():

	inputvalue= int(input("enter how many input you want to put : "))

	arr= []
	for i in range(inputvalue):
		element = input(f"enter the element {i+1}: ")
		arr.append(element)

	print("sorted element: ", Insertion(arr))

if __name__ == '__main__':
	main()