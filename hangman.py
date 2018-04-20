#!/usr/bin/env python
# hangman.py
# by Jaron Patena

correctWord = list("chicken")
guessWord = []
for j in range(0, len(correctWord)):
	guessWord.insert(j, '-')

while True:
	userInput = raw_input('Enter: ')

	# iterate the string
	for i in range(0, len(correctWord)):
		# if userinput is in each letter of word
		if correctWord[i] == userInput:
			del guessWord[i]
			guessWord.insert(i, userInput)

	print " ".join(guessWord)