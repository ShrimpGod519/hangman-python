import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

hangmancounter = 0

print(HANGMANPICS[hangmancounter] + "\n")

def get_guess(x,y):
  dashes = "-" * len(secret_word)
  guesses_left = 6
  
  while guesses_left > 0 and not dashes == secret_word:
    
    print(dashes)
    print (str(guesses_left) + " tries left")
    
    guess = input("Guess: ")
    
    if len(guess) != 1:
      print ("Your guess must have exactly one character!")
      
    elif guess in secret_word:
      print ("That letter is in the secret word!")
      dashes = update_dashes(secret_word, dashes, guess)
      if x < 7:
        print(y[x])
        
    else:
      print ("That letter is not in the secret word!")
      guesses_left -= 1
      x += 1
      if x < 7:
        print(y[x])
		
  if guesses_left <= 1:
    print ("You lose. The word was: " + str(secret_word))
  
  else:
    print ("Congrats! You win. The word was: " + str(secret_word))

def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess
      
    else:
      result = result + cur_dash[i]
      
  return result

with open('words.txt') as f:
    words = f.read().splitlines()


secret_word = random.choice(words)
get_guess(hangmancounter,HANGMANPICS)
