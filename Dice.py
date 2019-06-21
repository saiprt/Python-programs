import random
min = 0
max = 3
roll_again = "yes"

while roll_again == "yes" or (roll_again == "y" or roll_again==	"Y"):
	print("rolling Dice")
	print("The values are:")
	print(random.randint(min,max))
	print(random.randint(min,max))
	
	roll_again = str(input("Roll the dice again?(Y/N)"))
