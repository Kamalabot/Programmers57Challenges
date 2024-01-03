# With loop
def calculateSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum  # return the sum of the numbers 1 to n


# With recurse
def calcSumRecurse(n):
    if n == 0:
        return 0
    print(f"Working on {n}")
    return n + calcSumRecurse(n - 1)


# with formula
def calcSumMath(n):
    return n * (n + 1) / 2


print(calcSumRecurse(10))
print(calcSumRecurse(120))

print(calcSumMath(10))
print(calcSumMath(120))