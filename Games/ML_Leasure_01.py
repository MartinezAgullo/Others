# Pablo Martinez Agullo
# Leisure time: Probabilitat and guess the number
# 30/30/2019

#!/usr/bin/python3
import random

def main():
	print("Hello")
	print("What's your name? \n")
	Name = input()
	print("\nIt is good to meet you, " + Name)
	
	exit_game = False
	while exit_game == False: # Come to this point after each game
		print("Which game do you want to play?")
		print("A) Probabilitat")
		print("B) Guess the number")
		print("C) Dragon Realm")
		print("D) Hang Man")
		print("X) Exit")
		game = input()
		while game != 'A' and game != 'a' and game != 'B' and game != 'b' and game != 'C' and game != 'c' and game != 'x' and game != 'X'  and game != 'exit':	# if game not correctly chosen
			print("\nSorry, I could not understand your answer. Please choose A, B or X")
			print("Which game do you want to play?")
			print("A) Probabilitat")
			print("B) Guess the number")
			print("C) Dragon Realm")
			print("D) Hang Man")
			print("X) Exit \n")
			game = input()
		
		if game == 'A' or game =='a': Probabilitat(Name)		# Play probabilitat
		if game == 'B' or game =='b': GuessNumber(Name)			# Play guess the number
		if game == 'C' or game =='c': DragonRealm(Name)			# Play dragon's realm
		if game == 'D' or game =='d': HamgMan(Name)			# Play dragon's realm
		if game == 'X' or game =='x' or game == 'exit': exit()	# Exit




# Games definition
def Probabilitat(Name): 
	print("\nWe are playing probabilitat. Do you need a reminder of the rules?")
	aiuda = input()
	if aiuda == "Yes" or aiuda == "yes" or aiuda == "y" or aiuda == "Y":
		print("\nI will challenge you you to do something (in this case upon your suggest) and you will say a number which we name 'Probabilat' and it represents how unlikely or ill-fitting this is for you. In other words, this represents the inverse of the chance to do it: Probability = 1/'Probabilitat'. Then we both say at same time a number between 1 and 'Probabilitat' and, if both of us say the same number, you have to do whatever the challenge was. Remember that this is only fun when the number is not very high.")
	print("What am I going to challenge you to do?") 
	Challenge = input()
	print("Probabilitat of you '"+Challenge+"'?")
	probabilitat = insertInteger()
	MyNum = random.randint(1, probabilitat)
	print("Insert your number at 3, 2, 1... \n")
	YourNum = insertInteger()
	print("\n"+str(MyNum))
	if MyNum == YourNum:  #Same
		print("Well, well, "+Name+", it looks like you have to accept the challenge."+"\n")
	if (MyNum - YourNum) == 1 or (YouNum - MyNum) == 1:
		print("Uff Almost! You are saved"+"\n")
	else:
		print("You are saved"+"\n")
	return


def GuessNumber(Name):
	print("\n"+"We are playing to guess number. Do you need a reminder of the rules?"+"\n")
	aiuda = input()
	print("\n")
	if aiuda == "Yes" or aiuda == "yes" or aiuda == "y" or aiuda == "Y":
		print("It is simple, I will think a number and you will try to guess it. Let's start" +"\n")
	print("In which range (from 0 to __) do you want the number to be?"+"\n")
	theRange = input() # upper bound for de random number command
	print("\n")
	theRange = insertInteger()
	myNum = random.randint(1,theRange)	# Random number to be guessed
	print("I have already thought a number between 0 and " + str(theRange) + ". Try to guess it:" + "\n")
	guessTaken = 0 #This counts how many tries the player needed
	Success = False
	while Success == False:			# While the number is not known
		guessTaken = guessTaken+1	# Counter growth
		guess = insertInteger()
		if guess == myNum: Success = True		
		if guess < myNum: print("Too low. Try again: "+"\n")
		if guess > myNum: print("Too high. Try again: "+"\n")
		#else: print("Error, the answer was: " + str(myNum))	# This else should not be accessed 
	
	if guessTaken == 1:
		print("Congratularions, " + Name + "!!" +"\n"+"You guessed the number at the first try!!")
		print ("There was a probability of " + str(100/theRange) + " % of doing so!" + "\n")
	else:	
		print("Good job, " + Name + "! You guessed my number in "+ str(guessTaken) + " guesses!" +"\n")	
	return



def insertInteger():
	intger_error = True
	while intger_error == True:
		integer = input()
		try:
			integer=int(integer)
			if integer < 1: print("\n"+"The number you introduce should be an integer greater than zero." + "\n")
			else: intger_error = False
		except: print("\n"+"The input must be an integer" + "\n")
	return integer


def DragonRealm(Name):
	import time
	playAgain = "yes"
	while playAgain == "yes" or playAgain == "y" or playAgain == "Y" or playAgain == "Yes":
		print("You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight" +"\n")
		caveNumber = " "	 		# String
		while caveNumber != "1" and caveNumber != "2":
			print('Which cave will you go into? (1 or 2)')
			caveNumber = input()
		print("You approach the cave...")
		time.sleep(2)
		print("It is dark and spooky...")
		time.sleep(2)
		print("A large dragon jumps out in front of you! He opens his jaws and...")
		print()
		time.sleep(2)
		
		friendlyCave = random.randint(1, 2) # We randomly decide which cave is the dangerous
		
		if caveNumber == str(friendlyCave): print("Gives you his treasure!")
		else: print("Gobbles you down in one bite"+"\n")	
			
		print('Do you want to play again? (yes or no)')
		playAgain = input()
	return

	
def HangMan():
	  HangMan_Pics= ['''
+---+
	|
	|
	|
   ===''', '''
+---+
  O |
	|
	|
   ===''', '''
 +---+
   O |
   | |
     |
   ===''', '''
 +---+
   O |
  /| |
     |
    ===''', '''
 +---+
   O |
  /|\|
     |
    ===''', '''
 +---+
   O |
  /|\|
  /  |
    ===''', '''
 +---+
   O |
  /|\|
  / \|
    ===''']





if __name__ == '__main__':
    main()
