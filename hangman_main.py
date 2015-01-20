#Hangman Game
#
#The classic game of Hangman. The computer picks a random Word
#and the player wrong to guess to guess it. One letter at a time. If the player
#can't guess the word in time. the little stick figure gets hanged.

#importing random module

import random

#hangman constants


HANGMAN = ("""
 ________
 |      |
 |      |
 |
 |
 |
 |
 |
 |
 |
 |
 |
_|___________

 """,

 """          
 ________
 |      |
 |      |
 |      O
 |
 |
 |
 |
 |
 |
 |
 |
_|___________   

 
 """,
           


 """

 ________
 |      |
 |      |
 |      O
 |     -+-
 |
 |
 |
 |
 |
 |
 |
_|___________  


 """,

 """
 ________
 |      |
 |      |
 |      O
 |    /-+-
 |
 |
 |
 |
 |
 |
 |
_|___________


""",



"""

 ________
 |      |
 |      |
 |      O
 |    /-+-/
 |
 |
 |
 |
 |
 |
 |
_|___________


""",

"""
 ________
 |      |
 |      |
 |      O
 |    /-+-/
 |      |
 |
 |
 |
 |
 |
 |
_|___________

 """,


  """

 ________
 |      |
 |      |
 |      O
 |    /-+-/
 |      |
 |      |
 |     |
 |     |
 |
 |
 |
_|___________


  """,

  """
 ________
 |      |
 |      |
 |      O
 |    /-+-/
 |      |
 |      |
 |     | |
 |     | |
 |
 |
 |
_|___________


 """

)

#Because we start with an index of zero in a tuple we can just say that of guesses before game over will be one less than length

MAX_WRONG = len(HANGMAN)-1


WORDS = ("OVERUSED","CLAM","GUAM", "TAFFETA" , "PYTHON")

#Next is initializing the variable to a random word

word = random.choice(WORDS)

so_far = "-"*len(word) #one dash for each letter in the word

wrong = 0

used= []

#creating the main game loop

print("Welcome to Hangman, Good Luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess =input("\n\nEnter your guess: ")
    guess = guess.upper()

#Getting the Player's Guess 

    while guess in used:
        print("You've already guesses the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)
    
#checking the guess
    
    if guess in word:
        print("\nYes!", guess , "is the word!")

        #create a new so_far to include the guess

        new = " "

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\n Sorry ,", guess ,"isn't in the word.")

if wrong ==MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it")

print("\nThe word was", word)

input("\n\n Press the enter key to exit.")


        







