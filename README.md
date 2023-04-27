# wordle

A playground for me to experiment with different strategies of solving wordle.

Currently I just provide a tool for filtering the list of possible words based on information I get from guesses.

Filters work similar to as if I was using grep. There are essentially 4 patterns:

`..n..`

This matches words that have one or more a-z character at a known position. the '.' character indicates I do not know
what this character is.

`!....n`

This effectively the inverse of the previous filter.. This excludes characters that I know do not exist in a given position.

`abcd`

A string of characters with no `.` indicate these are letters I know exist in the final word, but I do not know the position of them.

`!defg`

A string of characters with no `.` that I know do not exist in the final word.

The script will prompt for filters, and multiple filters can be given, for example:

 .itas !bomvp !t.... 

Matches words ending in itas, the word does not contain bomvp, and t is not the first character. Results:

['ditas', 'litas']

Also added a script wordle_play.py which will pick a random word and will allow you to play.