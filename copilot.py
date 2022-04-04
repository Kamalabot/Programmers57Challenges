def calculateSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum  # return the sum of the numbers 1 to n

with open('Programmers57Challenges\empl_read.txt') as f:
    data = f.read()
    print(data)