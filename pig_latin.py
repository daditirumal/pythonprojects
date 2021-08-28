""" Writting a code to covert the regular sentence into a pig latin sentence"""

def piglatin(word):
    """ IN this function changing word to a pig latin word"""
    vowels = "aeiou"
    if word[0] in vowels:
        new_word = word[1:] + word[0] + "way"
    else:
        new_word = word[1:] + word[0] + "ay"
    return new_word


USER = ""
sentence = input("Enter any full sentence i will change into piglatin sentence \n")
words= sentence.split()
for i in enumerate(words):
    if USER == "":
        USER += piglatin(words[i])
    else:
        USER += " " +  piglatin(words[i])
print(USER)
