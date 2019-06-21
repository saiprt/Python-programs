def fib(num):
	a,b = 0,1
	while a<num:
		print(a, end=' ')
		a,b = b,a+b
	print()

def fib2(num):
	result=[]
	a,b=0,1
	while a<num:
		result.append(a)
		a,b=b,a+b
	print(result)
	
	
	
if __name__ == "__main__":
	print("this program is executing")
	print("____Fibonacci Series_____")
	import sys
	num=int(sys.argv[1])
	fib(num)
	fib2(num)
	

