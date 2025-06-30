def asc_des_none(lst: list, string: str) -> list:
    result = []
    if string == 'Asc':
        result = sorted(lst)
    elif string == 'Des':
        result = lst[::-1]
    else:
        result = lst

    return result


print(asc_des_none([4, 5, 2, 1], "Asc"))
print(asc_des_none([7, 8, 11, 66], "Des"))
print(asc_des_none([1, 2, 5, 6], "None"))
