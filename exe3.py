# Lets print some quotes
quote = input("What is the quote?")
who = input("Who said it?")

print(f"{who} says,\"{quote}\"")

#I can pull-in Data about other quotes and display here

with open('quotes_data.txt','+a') as text:
    text.write(quote, who)
    text.write('\n')
