def factorial(num: int) -> int:
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact


print(factorial(5))
