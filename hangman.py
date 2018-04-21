#!/usr/bin/env python
# hangman.py
# by Jaron Patena

def printMan(misses):
	print(" +---+\n |   |")
	if misses == 0:
		print("     |\n     |\n     |")
	if misses == 1:
		print(" O   |\n     |\n     |")
	elif misses == 2:
		print(" O   |\n |   |\n     |")
	elif misses == 3:
		print(" O   |\n/|   |\n     |")
	elif misses == 4:
		print(" O   |\n/|\\  |\n     |")
	elif misses == 5:
		print(" O   |\n/|\\  |\n/    |")
	elif misses == 6:
		print(" O   |\n/|\\  |\n/ \\  |")
	print("     |\n=======")

# setup
correctWord = list("spaghetti")
guessWord = []
wrongInputs = []
for j in range(0, len(correctWord)):
	guessWord.insert(j, '-')

# main
while len(wrongInputs) < 6:
	printMan(len(wrongInputs))
	print "Missed: " + ", ".join(wrongInputs)
	print "Word: " + " ".join(guessWord)
	userInput = raw_input('Guess: ')
	print "\n"

	gotItRight = False

	# iterate the string
	for i in range(0, len(correctWord)):

		# if userinput is in each char of word
		if correctWord[i] == userInput:
			del guessWord[i]
			guessWord.insert(i, userInput)

			# flag when guessed right
			gotItRight = True

	# record wrong input
	if gotItRight == False:
		wrongInputs.append(userInput)

	if guessWord == correctWord:
		print("you win!")
		break

if len(wrongInputs) == 6:
	printMan(6)
	print("game over!")

