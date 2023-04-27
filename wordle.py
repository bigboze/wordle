import string
import readline
import itertools
from enum import Enum

"""
Tool for filtering words based on known and unknown characters in wordle.
"""

def filter(words: list, chars: list):
  """ filters words that contain all characters in chars where the position
      of each char is unknown
  """
  return [word for word in words if all(c in word for c in chars)]

def filter_not(words: list, chars: list):
  """ filters words that contain non of the characters in chars
  """
  return [word for word in words if all(c not in word for c in chars)]

def filter_positioned(words: list, pattern: str):
  """filters words based on characters that are of a known position.
     The pattern is a string of characters and periods. The periods represent an
     unknown character. The characters represent a known character.

     eg:

     the pattern "cr.nk" filters to 
    ['crink', 'cronk', 'crunk', 'crank']
  """
  return [word for word in words if all(c == '.' or pattern[i] == word[i] for i, c in enumerate(pattern))]

def filter_positioned_not(words: list, pattern: str):
  """similar to filter_positioned. Filters words where characters are not present in
     known positions.
  """
  return [word for word in words if all(c == '.' or pattern[i] != word[i] for i, c in enumerate(pattern))]

class MatchResult(Enum):
  NOT_IN_WORD = 0,
  IN_WORD = 1,
  POSITIONAL_MATCH = 2,

# all of the possible match patterns for a given input
# 3^5 = 243 combinations
patterns = itertools.product([MatchResult.NOT_IN_WORD, MatchResult.IN_WORD, MatchResult.POSITIONAL_MATCH], repeat=5)

# currently not used. Idea is to run this for every match pattern result to obtain
# how much information is gained from a given match pattern. We can use this to give 
# some heuristic as to what words give the most information. 
def filter_match_result(pattern, guess, words):
  """
  Constructs and perform filters based on a match pattern and return the result.
  """
  not_in_word = ''
  in_word = ''
  in_position = '.....'
  not_in_position = '.....'
  
  for i, result in enumerate(pattern):
    if result == NOT_IN_WORD:
      not_in_word += guess[i]
    elif result == IN_WORD:
      in_word += guess[i]
      not_in_position += guess[i]
    elif result == POSITIONAL_MATCH:
      in_position = guess[i]

  if len(not_in_word) > 0:
    words = filter_not(words, not_in_word)
  if len(in_word) > 0:
    words = filter_not(words, in_word)
  if in_position != '.....':
    words = filter_positioned(words, in_position)
  if not_in_position != '.....':
    words = filter_positioned_not(words, not_in_position)
  
  return words

def load_words():
  with open('words.txt', 'r') as f:
    return f.read().splitlines()

words = load_words()
total_words = len(words)

print("Please enter guess information:")
while True:
  ln = input().strip().split()
  for pattern in ln:
    if pattern[0] == '!':
      if pattern.find('.') >= 0:
        words = filter_positioned_not(words, pattern[1:])
      else:
        words = filter_not(words, pattern[1:])
    else:
      if pattern.find('.') >= 0:
        words = filter_positioned(words, pattern)
      else:
        words = filter(words, pattern)

  if len(words) == 1:
    print("The word is: " + words[0])
    break
  if len(words) == 0:
    print("no words found, resetting")
    words = load_words()
    
  print(words)

