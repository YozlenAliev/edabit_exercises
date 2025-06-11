def series_resistance(number) -> str:
    result = 0
    for num in number:
        result += float(num)
    if result > 1:
        return f'{abs(result)} ohms.'
    return f'{abs(result)} ohm.'


res_values = input().split(', ')
print(series_resistance(res_values))
