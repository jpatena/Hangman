#!/usr/bin/env python
# hangman.py
# by Jaron Patena

correctWord = list("chicken")
guessWord = []
wrongInputs = []
for j in range(0, len(correctWord)):
	guessWord.insert(j, '-')

while len(wrongInputs) < 6:
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
	print("game over!")