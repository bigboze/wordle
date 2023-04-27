import random
import readline

def load_words():
  with open('words.txt', 'r') as f:
    return f.read().splitlines()

words = load_words()

the_word = random.choice(words)

guesses = []
max_guesses = 6

def guess_result(guess, the_word):
  resl = [0, 0, 0, 0, 0]
  for i, char in enumerate(guess):
    if char == the_word[i]:
      resl[i] = 2
    elif char in the_word:
      resl[i] = 1
  return resl

def render_guess(guess, the_word):
  out = ''
  hint = ''
  for i, char in enumerate(guess):
    if resl[i] == 0:
      out += '.'
      hint += ' '
    elif resl[i] == 1:
      out += '.'
      hint += '*'
    else:
      out += guess[i]
      hint += ' '
  print(out)
  print(hint)

while True:
  print("Enter guess:")
  guess = input().strip()

  if guess not in words:
    print(f'"{guess}" is not a valid word')
    continue

  resl = guess_result(guess, the_word)
  
  if sum(resl) == 10:
    print(f"You guessed the word! {the_word} in {len(guesses)} guesses")
    break
  guesses.append(resl)
  
  if len(guesses) >= max_guesses:
    print(f"You ran out of guesses! The word was {the_word}")
    break

  render_guess(guess, the_word)

  
