def Factorial(n):
    if n > 1:
        return n * Factorial(n-1)
    return 1

print(Factorial(0))
print(Factorial(1))
print(Factorial(5))