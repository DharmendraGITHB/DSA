#full reversing array 

n=int(input())    #user input 

m=input().strip().split(' ')  
res= m[::-1]                 #reverse the list by slicing method
r=""
for i in range(n):
    r= r+ str(res[i])+ " "

print(r)
