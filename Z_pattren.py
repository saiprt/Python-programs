def pattern(line):
	top,bottom,diagonal = 1,1,(line-1)
	for i in range(0,line):
		print(top, end=' ')
		top+=1
	print()
	for j in range(1,line-1):
		for index in range((line-j-1)):
			print(" ",end=" ")
			
		print(diagonal, end=' ')
		diagonal-=1
		print()
	for z in range(line):
		print(bottom, end=' ')
		bottom+=1
	print()	

import sys
line=int(sys.argv[1])
pattern(line)
pattern(line+3)		
	