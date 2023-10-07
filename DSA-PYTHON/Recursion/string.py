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

""" this is not the optimal solution """

""" 
reverse_string_recursive("Hello, World!")
  reverse_string_recursive("ello, World!")
    reverse_string_recursive("llo, World!")
      reverse_string_recursive("lo, World!")
        reverse_string_recursive("o, World!")
          reverse_string_recursive(", World!")
            reverse_string_recursive(" World!")
              reverse_string_recursive("World!")
                reverse_string_recursive("orld!")
                  reverse_string_recursive("rld!")
                    reverse_string_recursive("ld!")
                      reverse_string_recursive("d!")
                        reverse_string_recursive("!") (Base case)



reverse("hello")
|
|--- reverse("ello") + "h"
|    |
|    |--- reverse("llo") + "e"
|    |    |
|    |    |--- reverse("lo") + "l"
|    |    |    |
|    |    |    |--- reverse("o") + "l"
|    |    |    |    |
|    |    |    |    |--- reverse("") + "o"
|    |    |    |    |    |
|    |    |    |    |    |--- ""
|    |    |    |    |  
|    |    |    |    |--- "o"
|    |    |    |
|    |    |    |--- "ol"
|    |    |    |  
|    |    |--- "llo"
|    |  
|    |--- "olle"
|  
|--- "olleh"


"""