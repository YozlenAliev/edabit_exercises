def is_curzon(num):
    if ((2 ** num) + 1) % ((2 * num) + 1) == 0:
        return True
    return False

number = int(input())
print(is_curzon(number))