from string import ascii_uppercase
import random

alph = list(ascii_uppercase)
secret_word = ["Elephant",'Fish']
word_play = random.choice(secret_word).upper()
hint = ['_'] * len(word_play)

ascii_hangman_art = {0 : ('   ',
                          '   ',
                          '   '),
                     1 : (' O ',
                          '   ',
                          '   '),
                     2 : (' O ',
                          ' | ',
                          '   '),
                     3 : (' O ',
                          ' |\\',
                          '   '),
                     4 : (' O ',
                          '/|\\',
                          '   '),
                     5 : (' O ',
                          '/|\\',
                          '  \\'),
                     6 : (' O ',
                          '/|\\',
                          '/ \\')}

def display_alph(alph: list, guess):
     for char in alph:
          if guess == char:
               alph.remove(guess)
     print(alph)

def display_hint(hint: list, char_guess):
     if char_guess in word_play:
          for i in range(len(word_play) + 1):
               guess_index = word_play.index(char_guess, i)
               hint[guess_index] = char_guess
               if hint.count(char_guess) == word_play.count(char_guess):
                    break
     print(hint)

def display_hangman(hangman_art: dict, wrong_guess:int):
     for line in hangman_art.get(wrong_guess):
          print(line, end= '\n')

def main():
     wrong_guess = 0
     is_playing = True
     guessed_alph = 0
     
     while is_playing:
          guess = input("Guess the letter: ").upper()
          if guess in word_play:
               if guess in alph:
                    guessed_alph += word_play.count(guess)
               elif guess.isalpha() and guess not in alph:
                    print(f'{guess} already guessed')
               else:
                    print('Please enter a letter')
          display_hint(hint, guess)
          print(guessed_alph)
          display_alph(alph, guess)
          if guess not in word_play:
               wrong_guess += 1
          display_hangman(ascii_hangman_art, wrong_guess)
          if guessed_alph == len(word_play):
               is_playing = False
               print('You win!😁')
          elif wrong_guess == 6:
               is_playing = False
               print('You lose!')

if __name__ == '__main__':
    main()