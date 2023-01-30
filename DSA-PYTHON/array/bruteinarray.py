class bruteforce:
	def __init__(self, arr):
		self.arr = arr


	def search(self, target):
		for i in range(len(self.arr)):
			if self.arr[i] == target:
				return i


		return -1


arr = [1,2,3,4,5,6,7,8,9]
target = 5
b= bruteforce(arr)
result = b.search(target)



if result != -1:
	print("target found at index:", result)

else:
	print("target not found in the array")


""" time complexity of this code is O(n), where n is the number of elements in the array.
this is worst case. the algo wil have to iterate through all n elements in the array 



space complexity o(1)


to improve time complexity of this we need to try other algorithms like binary search.

dk

"""