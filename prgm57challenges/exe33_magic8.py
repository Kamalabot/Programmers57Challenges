#Magic 8 game

"""This is a game which answers the question"""

answer = ['Yes','No','Maybe','Ask Again Later']

import random

from scipy import rand
#Gets question
trial = input("What is your question? ")
#Shuffles the list of answers
random.shuffle(answer)
#Gets Random number between 0 and 3
qR = random.randint(0,3)
#Replies
print(answer[qR])