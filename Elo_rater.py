#Elo rating provided by finxter site for python mastery

"""This program will start with an Elo rating and calculate
new rating based on the recent correct or wrong answer"""


def elo_rate(current_score: int, answer: str) -> int:

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


cond_dict = {'l5': {'Correct': 41,
                    'Incorrect': -14},
             '1k': {'Correct': 16,
                    'Incorrect': -39},
             '2k': {'Correct': 8,
                    'Incorrect': -47}
             }


def elo_dict(current_score: int, answer: str):
    # check the smallest first
    if current_score < 500:
        current_score = current_score + cond_dict['l5'][answer]
    # check whether the number is bigger first
    elif current_score < 2000 or current_score > 1000:
        current_score = current_score + cond_dict['2k'][answer]
    # then check if it is smaller
    elif current_score < 1000 or current_score > 500:
        current_score = current_score + cond_dict['1k'][answer]
 
    return current_score


print(elo_dict(550, 'Correct'))  # 566
print(elo_dict(350, 'Correct'))  # 391
print(elo_dict(1050, 'Correct'))  # 1066
print(elo_dict(1550, 'Correct'))  # 1558

print(elo_dict(550, 'Incorrect'))  # 511
print(elo_dict(350, 'Incorrect'))  # 336
print(elo_dict(1050, 'Incorrect'))  # 1011
print(elo_dict(1550, 'Incorrect'))  # 1503