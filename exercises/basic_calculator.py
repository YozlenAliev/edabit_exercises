def calculator(num1: int, operator: str, num2: int) -> str | int:
    result = 0
    if operator == '/' and num2 == 0 or num1 == 0:
        return "Can't divide by 0!"
    else:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '/':
            result = num1 / num2
        elif operator == '*':
            result = num1 * num2
    return result


number_1 = int(input())
operator = input()
number_2 = int(input())

print(calculator(number_1, operator, number_2))
