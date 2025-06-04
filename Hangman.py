# Hangman game :)

# Why did I make this work so weird

from words import wordlist
from random import choice
from os import system
# Btw I use os to exit because I don't like the python exit

tries = 6
letterguesses = 0

print("Hangman")
print("made by ChrisjL1002 :)")
print("")

word = choice(wordlist)
wordlen = len(word)

def guess():
    global letterguesses
    # Why do I use global SO MUCH I don't get it
    if letterguesses == wordlen:
        return input("Do you know the word yet? you guessed all the letters, word: ")
    return input("Guess: ")

def guess_check(guess):
    # Idk how tf this function works
    global letterguesses
    global word
    global tries
    # Global hell
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
    print("")
    print(f"You got it! The word was {word}!")
    system("exit")

def fail():
    print("")
    print(f"You didn't get it :( The word was {word}.")
    system("exit")

print(f"Word length: {wordlen}")
print("")
c = "I hate python so much"

while tries != 7:
    if c == "Correct!":
        correct()
    elif tries == 0:
        tries = 7
        print("")
        fail()
    else:
        g = guess()
        c = guess_check(g)
        print(c)

# I made this much cleaner
