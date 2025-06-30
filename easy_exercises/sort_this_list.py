def asc_des_none(lst: list, order: str) -> list:
    result = []
    if order == 'Asc':
        result = sorted(lst)
    elif order == 'Des':
        result = lst[::-1]
    elif order == 'None':
        result = lst
    return result


numbers = input().split(', ')
sorting_type = input()
result = asc_des_none(numbers, sorting_type)
final_lst = []
for num in result:
    final_lst.append(int(num))

print(final_lst)
