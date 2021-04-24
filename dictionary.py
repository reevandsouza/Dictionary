'''
This is a simple working dictionary
'''
#importing the necessary modules needed
import json
from difflib import get_close_matches
# loading the main dictionary json file
data = json.load(open("data.json"))

# Main word search/match algorithm
def check_word(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Word does not exist in the dictionary")
        else:
            return("Please enter y or n")
    else:
        return ("Please enter valid word")

# This is useful for words that have multiple meanings
word = input("Enter the word to be searched: ")
meaning = check_word(word)
if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)




