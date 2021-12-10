# To clean the console, so only the program can be seen:
from os import system
system("cls")

# Ask the user for a sentence and the length the word should have to be flip
sentence = input("Please introduce the word or the sentence you want to flip:\n>")

word_length = int(input("Please enter the length that the word must have to get flipped:\n>"))

# Transform the sentence into a list with strings inside
words = sentence.split()

# Loop to walk though the list:
for word in words:

    # Checks if the word should be flipped based on how many characters it has
    if len(word) >= word_length:

        word_index = words.index(word) # Saves the index of the word which meets the condition
        words[word_index] = word[len(word)::-1] # Flips and saves the word into the list or words

# Joins the words inside the list to make the same sentence from the beginning
# But that words that meets the condition to be flip, they are flipped in the sentnece
print(" ".join(words)) 