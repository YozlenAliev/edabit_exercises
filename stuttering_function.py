def stutter_word(a: str) -> str:
    return f"{a[0:2]}... {a[0:2]}... {a}?"


stutter = input()
print(stutter_word(stutter))