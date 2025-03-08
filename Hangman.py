# Hangman game :)

# My name is Edwin.
# I made the Mimic.
# It was difficult to put the pieces together.
# But unfortunately, something went so wrong, and now I can't do anything, BUT SING THIS STUPID SONG!!!!

import words
import random
import os

tries = 6
letterguesses = 0

print("Hangman")
print("made by ChrisjL1002 :)")
print("")

word = random.choice(words.wordlist)
wordlen = len(word)

def guess():
    global letterguesses
    if letterguesses == wordlen:
        return input("Do you know the word yet? you guessed all the letters, word: ")
    return input("Guess: ")

def guess_check(guess):
    global letterguesses
    global word
    global tries
    positions = [i + 1 for i, letter in enumerate(word) if letter == guess]
    if guess == word:
        tries = 7
        return "Correct!"
    elif positions:
        letterguesses=letterguesses+1
        return f"Letter in postiton/s {positions}. Tries left: {tries}"
    elif len(guess) > 1:
        tries=tries-1
        return f"{guess} is not the word. Tries left: {tries}"
    else:
        tries=tries-1
        return f"Letter not in word. Tries left: {tries}"

def correct():
    global word
    print("")
    print(f"You got it! The word was {word}!")
    os.system("exit")

def fail():
    print("")
    print(f"Incorrect! The word was {word}.")
    os.system("exit")

print(f"Word length: {wordlen}")
print("")
g = guess()
print("")
c = guess_check(g)

while tries != 7:
    print(c)
    if c == "Correct!":
        correct()
    elif tries == 0:
        tries = 7
        print("")
        fail()
    else:
        print("")
        g = guess()
        c = guess_check(g)