import random
number = random.randint(1,29)
with open("Words.txt","r") as f:
	for i in range(1,(number+1)):
		word = str(f.readline())

attempts = 15
		
name = str(input("Enter your name:"))		
print("Hi ",name," welcome to Hangman Game.Hava fun!")
length = (len(word)-1)
word_guess=""

print("You have to guess {} letters word now".format(length))
for dash in range(0,length): 
	print("_", end=" ")
print()
guess=str(input("Guess the first letter:"))
while attempts > 0:
	if guess[-1] in word[:-1]:
		print("you guessed letter correctly")
		for l in range(0,length):
			if guess[-1] == word[l]:
				print(guess[-1], end="")
				word_guess += guess[-1]
			else:
				print("_", end="")
		print()
	else:
		print("The letter you guessed is not in the word")
	attempts -=1
	fail=0
	for letter in word[:-1]:
		if letter in word_guess:
			#print("fail is same")
			pass
		else:
			fail = 1
			#print("fail is differ")
	if fail == 0:
		#print("fail is fail0")
		break
	print("You have {} attempts left".format(attempts))	
	new_letter= str(input("Enter your next guess:"))
	guess = guess + new_letter[0]	
			
if fail == 0:
	print("You Guessed the word ",word," in ",(15-attempts)," attempts.Congracts")
else:	
	print("better luck next time,You didn't guess the word")
	print("The actual word is:",word)	
		
	
	
	
		
	