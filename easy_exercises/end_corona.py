def end_corona(recovers: int, new_cases: int, active_cases: int) -> int:
    days = 0
    while active_cases > 0:
        active_cases += new_cases
        active_cases -= recovers
        days += 1
    return round(days, 2)


print((end_corona(30000, 25000, 390205)))
