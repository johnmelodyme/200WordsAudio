from random_word import RandomWords
import os as yourComputer

# Uncomment To Install 
#yourComputer.system("pip install Random-Word")

r = RandomWords()

# Return a single random word
word = r.get_random_word()
# Return list of Random words
words = r.get_random_words()
# Return Word of the day
word_of_the_day = r.word_of_the_day()
#while True:
print(words)
