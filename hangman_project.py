import random
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
Hangman = ['''
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
print("let's play Hangman")
print("You have maximum six lives")
player1 = []
guess_player1=random.choice(words)
count = 0
lives = 6
a=0
empty = []
for alphabet in guess_player1:
    player1.append(alphabet)
    count += 1
print(f"Guessed word has {count} letters")
for i in player1:
    empty.append("_")
print(empty)
while lives != 0 and empty != player1:
    guess_player2 = input("guess a letter:")
    for i in range(0, len(player1) - 1):
        if guess_player2 == player1[i]:
            empty[i] = guess_player2
            print(empty)
            continue
    else:
        if guess_player2 not in player1:
            lives -= 1
            print(f"you lose 1 life,you have {lives} lives left")
            print(f"{Hangman[a]}")
            print(f"attempts left:{lives}")
            a=a+1
            if lives==0 :
                print("you have been HANGED")
                print("you lose")
                if empty==guess_player1 :
                    print("you guessed it correctly")
                    print("    you won")