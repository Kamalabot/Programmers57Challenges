# Counting Characters

in_str = input("What is the input string? ")

if len(in_str) == 0:  # check if the characters are entered
    print("Please enter something to compute")
else:  # return the num of characters
    print(f"{in_str} has {len(in_str)} characters")
