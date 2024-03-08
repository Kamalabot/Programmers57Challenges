#Lets count the word frequency in the text block

"""Takes a block of text and finds the 
frequency of each word in the text"""

file = input("Do you have a file with words? (y/n) ")
if file == 'y':
    inp = input("Enter the file name: ")
    with open(inp, 'r') as f:
        text = f.read()
else:  
    text = input("Enter a your text: ")

listText = text.split(' ') #split the text into a list

#one of the solutions.
for txt in listText:
    print(txt, listText.count(txt))

striped_text = []
for txt in listText:
    striped_text.append(txt.strip(',.?!')) #This makes the important objects stand out    

#We can use the counter function from collections library
from collections import Counter

wordFreq = Counter(striped_text)

#sort the word frequency in descending order

sort_wfreq = sorted(wordFreq.items(),key= lambda x: x[1], reverse=True)
print(sort_wfreq)       

#Creating the bar chart with stars

for word, freq in sort_wfreq[:3]:
    print(f"{word}:", end = ' ')
    print('*' * freq)