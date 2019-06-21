def pattern(line):
	pat= " "
	for i in range(0,line):
		for j in range(0,line):
			if(((j==1 or j==(line-2)) and i!=0 and i!=(line-1)) or
				(i==((line-1)/2) and j>1 and j<(line-1)) or
				((line%2==0) and i==(line/2) and j!=0 and j!=(line-1))):
					pat=pat+"*"
			else:
				pat=pat+" "
		pat=pat+"\n"
	return pat

import sys
line=int(sys.argv[1])
print(pattern(line))	