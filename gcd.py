def find_gcd(x,y):
	while(y):
		x,y = y,x%y
		
	return x

import sys
l = sys.argv[1:]
num1=int(l[0])
num2=int(l[1])
gcd1 = find_gcd(num1,num2)

for i in range(2,len(l)):
	gcd1 = find_gcd(gcd1,int(l[i]))
	
print("G.C.D for given numbers is:",gcd1) 
