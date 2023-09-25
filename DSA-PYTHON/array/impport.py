class CustomArray:
    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

def main():
    user_input = int(input("Enter the number of elements you want to sort: "))
    arr = []

    for i in range(user_input):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    custom_array = CustomArray(arr)
    custom_array.bubble_sort()

    print('Sorted array:', custom_array.arr)

if __name__ == "__main__":
    main()
