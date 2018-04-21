#!/usr/bin/env python
# hangman.py
# by Jaron Patena

correctWord = list("chicken")
guessWord = []
for j in range(0, len(correctWord)):
	guessWord.insert(j, '-')
miss = 0

while miss < 6:
	userInput = raw_input('Enter: ')

	gotItRight = False

	# iterate the string
	for i in range(0, len(correctWord)):
		# if userinput is in each char of word
		if correctWord[i] == userInput:
			del guessWord[i]
			guessWord.insert(i, userInput)

			# flag when guessed right
			gotItRight = True

	# increment when guessed wrong
	if gotItRight == False:
		miss = miss + 1

	print miss
	print " ".join(guessWord)