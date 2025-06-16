def calculate_damage(damage_: int, speed_: int, time_: str) -> int | str:
    result = 0
    if damage < 0 or speed < 0:
        return f'Invalid'
    else:
        if time_ == 'second':
            result = damage_ * speed_
        elif time_ == 'minute':
            result = damage_ * speed_ * 60
        elif time_ == 'hour':
            result = damage_ * speed_ * 3_600
    return result


damage = int(input())
speed = int(input())
time = input()

print(calculate_damage(damage, speed, time))
