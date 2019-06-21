import random

guesses = 0
number = random.randint(1,50)

while guesses < 5:
	guess = int(input("Enter your guess:"))
	guesses+=1
	print("This is your guess number:",guesses)
	if guess > number:
		print("clue:Your guess is larger than actual number")
	elif guess < number:
		print("clue:Your guess is smaller than actual number")
	elif guess == number:
		break
if guess == number:
	print("You guessed the correct number({0}) in {1} attempts".format(number,guesses))
elif guess != number:
	print("Better luck next time")
	print("The actual number is:{0}".format(number))
	