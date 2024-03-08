#Lets replace some words in our file, automatically

"""There are many occasions where we want a word in 
a file to be replaced with another, without opening that file."""

inp = input("Enter input file name: ")

out = input("Enter output file name: ")

from_wrd = input("Input the word to be replaced: ")

to_wrd = input("Input the replacement word: ")

updated_text =""
""" Not working the way I want
with open(inp) as f:
    data = f.readlines()
    for sent in data:
        words = sent.strip().split(' ')
        for word in words:
            if word == from_wrd:
                word = to_wrd
        new_words = ",".join(words)
        new_words =  new_words + '\n'
        updated_text = updated_text + new_words
"""
"Some the solution is very simple, so use it"

with open(inp) as f:
    data = f.read()
    data = data.replace(from_wrd, to_wrd)

with open(out, 'w') as f:
    f.write(data)
