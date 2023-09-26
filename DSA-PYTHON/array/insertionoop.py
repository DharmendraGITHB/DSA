

class Insertion:
	def __init__(self,arr):
		self.arr = arr

	def insertionsort(self):
		n = len(self.arr)

		for i in range(1,n):
			start_element = self.arr[i]
			j = i-1
			while j>=0 and self.arr[j]> start_element:
				self.arr[j+1] = self.arr[j]
				j -=1
			self.arr[j+1]= start_element

		return self.arr


def main():

	input_value = input("enter the input value: ")
	arr =[]
	for i in range(int(input_value)):
		element = input(f"Enter the element {i+1}:")
		arr.append(element)

	obj = Insertion(arr)
	obj.insertionsort()
	print("sorted array:", obj.insertionsort())


if __name__ == '__main__':
	main()