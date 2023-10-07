# reverse a string using recurison

def reverseString(str):
	if not str:
		return str 

	else:

		return reverseString(str[1:]) + str[0]

str = 'hello'

fun = reverseString(str)

print(fun)

# time complexity of this recursive algo is O(n), n is lenght of input

# space complexity of this recursive algorithm is O(n) as well, This is because for each recursive call a new stack frame is created to store the functions local variables 

