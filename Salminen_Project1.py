#!/usr/bin/python

#Name: Paul Salminen
#Email: paul.salminen@colorado.edu
#Project 1: Card guessing game
#Recitation: 114

import random
import string
import sys

#Create the random Card
def CardGenerator():
	Suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

	return (random.choice(Suits), random.randint(2,14))

#Changes picture card input into number for easier processing
def PictureCards(Card):
	Cards = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

	if Card in Cards:
		return Cards[Card]

	return(Card)
	
#Help user find number
def NumHelper(UserNumber, RealNumber):
	x = 0
	while x < 3:
		if UserNumber 	> RealNumber:
			UserNumber 	= raw_input("Nope! Your number is too high, idiot. Please try again: ")

		elif UserNumber < RealNumber:
			UserNumber 	= raw_input("Nope! Your number is too low, putz. Please try again: ")
			
		elif UserNumber == RealNumber:
			return(UserNumber)

		UserNumber = int(PictureCards(UserNumber))
		x += 1
	
	return(UserNumber)
			
#Help user find suit
def SuitHelper(UserSuit, RealSuit):
	n = 0
	while n < 2:
		if UserSuit != RealSuit:
			UserSuit = raw_input("Nope, come on! There aren't that many suits, try again: ")
		elif UserSuit == RealSuit:
			print("Look at you, you finally got the suit right!")
			n = 2
		n = n + 1
	return(UserSuit)
	
#Covert RandomNumber variable to name for picture card output
def PictureCards2(Number):
	if Number == 11:
		Number = "Jack"
	elif Number == 12:
		Number = "Queen"
	elif Number == 13:
		Number = "King"
	elif Number == 14:
		Number = "Ace"
	return Number

#Print out final findings
def Findings(Num,S):
	if Num == "True" and S == "True":
		print("Congrats! You actually guessed the card correctly. Your mom must be so proud.")
		Win = 1
	elif Num == "True" and S == "False":
		print("You found the correct number, but not the correct suit. You should try again, you don't want to quit a loser.")
		Win = 0
	elif Num == "False" and S == "True":
		print("You found the correct suit, but not the correct number. You should try again, you don't want to quit a loser.")
		Win = 0
	else:
		print("You didn't find any correct information about the card. You should try again, you don't want to quit a loser.")	
		Win = 0
	return Win

#Determine how many games have been played
def GameCounter(count=[]):
	count.append(1)
	Repeat = len(count)
	return Repeat

#Keep track of Wins
def WinLose(Success, count=[]):
	if Success == 1:
		count.append(1)
	return len(count)

def main():
	#Introduce the game and rules
	print("Care to play a game?")
	print("You are going to guess the card that I am thinking of, okay?")
	print("You will guess the number and suit, and then you will get clues to correct your guess.")
	print("You will have have 3 tries to find the correct number, and 2 tries to find the right suit.")
	
	#Import the random Card number and suit
	RandomSuit, RandomNumber = CardGenerator()
	
	#Input user's guess
	Guess = raw_input("What do you think the card is? (Ex. 4 of Hearts, or Jack of Spades) ")
	Guess = string.rsplit(Guess)
	GuessNumber = Guess[0]
	GuessSuit = Guess[2]
	GuessNumber = int(PictureCards(GuessNumber))
	
	#Help user find number
	GuessNumber = NumHelper(GuessNumber, RandomNumber)
	#Determine if Number was found
	if GuessNumber != RandomNumber:
		print("You're not going to get the number, and I'm bored now. Stop trying!")
		Number = "False"
	else:
		print("You got the right number!")
		Number = "True"
	
	#Help User find Suit	
	GuessSuit = SuitHelper(GuessSuit, RandomSuit)	
	#Determine if Suit was found
	if GuessSuit != RandomSuit:
		print("You've had more than enough tries, you just can't get this suit.")
		Suit = "False"
	else:
		Suit = "True"
	if RandomNumber > 10:
		RandomNumber = PictureCards2(RandomNumber)
	else:
		RandomNumber = RandomNumber
	
	#Find the number of times the game has been played
	Reps = GameCounter()	
	
	#Tell what card was
	CorrectAnswer = "I was thinking of the",RandomNumber,"of",RandomSuit
	print(CorrectAnswer)
	#Calculate stats
	WL = Findings(Number, Suit)
	Wins = WinLose(WL)
	Statement = "You have played",Reps, "times, and you have won",Wins,"times."
	print(Statement)
	#Ask to play again
	Again = raw_input("Do you with to play again?")
	Again = Again[0]
	Again = Again.lower()
	if Again == "y":
		main()
	elif Again == "n":
		sys.exit(0)
	else:
		print("You can't even answer that right, goodbye.")
		sys.exit(0)
	
main()
