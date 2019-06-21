def pattern(n):
	for i in n:
		print("/",end="")
		print("*" * int(i))
	'''In pyhton,Strings can be used in arithematic opearations'''
	
import sys

pattern(sys.argv[1])



