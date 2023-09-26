

class Selection:
	def __init__(self, arr):
		self.arr = arr


	def sorting(self):
		size = len(self.arr)
		
		for i in range(size-1):
			min_Val= i

			for j in range(i+1,size):
				if self.arr[j] < self.arr[min_Val]:
					min_Val = j
			self.arr[i], self.arr[min_Val] = self.arr[min_Val], self.arr[i]

		return self.arr


def main():

	inputval= int(input("enter how many input values you want: "))

	arr = []

	for i in range(inputval):
		try:
			element = int(input(f"enter an element {i+1}: "))
			arr.append(element)

		except ValueError:
			print("INVALID INPUT , PLEASE ENTER AN INTEGER")
			main()

	obj = Selection(arr)
	obj.sorting()

	print("sorted arr:", obj.sorting())


if __name__=="__main__":
	main()


"""
Number of comparisons: (n - 1) + (n - 2) + (n - 3) + ..... + 1 = n(n - 1) / 2 nearly equals to n^2
and time complexity = O(n^2)

"""