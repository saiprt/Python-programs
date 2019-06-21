class EmpCounter:
	'empoyee counts'
	empcount = 0
	Name=" "
	Age=0
	def __init__(self,name,age):
		self.name = name
		self.age = age
		EmpCounter.empcount+=1
		EmpCounter.Name= name
		EmpCounter.Age = age
		
		
	def display_empdetails(self):
		print("Name:",self.name,end=" ")
		print("Age:",self.age)
	
	def write_employee(self,line):
		
		with open("Sample.txt","a") as f:
			f.write(line+"\n")
		print("employee add successfully")
	
	
			
	
		
		print("Employee count is:",EmpCounter.empcount)
if __name__ == "__main__":
	option = input("press Y to enter details and R to see employees list:")
	if option == "Y":
		YesorNo = "Y"
	
		YesNO= " "
		
		while YesorNo == "Y":
			name1= input("enter Employee name:")
			age1=int(input("enter employee age:"))
			e1 = EmpCounter(name1,age1)
			line=str(EmpCounter.Name) + " " + str(EmpCounter.Age)	
			print(line)
			e1.write_employee(line)
			YesNO = input("want to Continue:(Y/N)")
			if YesNO == "Y" or "N":
					pass
					YesorNo = YesNO
			else:		
				while YesNO != "Y" and YesNO != "N":
					print("choose wrong option:")
					yesNo = input("want to Continue:(Y/N)")
	elif option == "R":
		print("you choose to see the employees list")
		with open("Sample.txt","r") as f:
			print(f.read())
		print("read employees suceessfully")
	else:
		print("wrong option selected")
				
		