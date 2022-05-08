#Elo rating provided by finxter site for python mastery
"""This program will start with an Elo rating and calculate
new rating based on the recent correct or wrong answer"""

def elo_rate(current_score: int, answer:str) ->int:

    if answer == 'Correct' and current_score < 500:
        current_score = current_score + 41

    elif answer == 'Incorrect' and current_score < 500:
        current_score = current_score - 14

    elif answer == 'Correct' and (current_score < 1000 or current_score > 500):
        current_score = current_score + 16
    
    elif answer == 'Incorrect' and (current_score < 1000 or current_score > 500):
        current_score = current_score - 39

    elif answer == 'Correct' and (current_score < 2000 or current_score > 1000):
        current_score = current_score + 8

    elif answer == 'Incorrect' and (current_score < 2000 or current_score > 1000):
        current_score = current_score - 47

    return current_score

print(elo_rate(550, 'Correct'))

print(elo_rate(1050, 'Incorrect'))