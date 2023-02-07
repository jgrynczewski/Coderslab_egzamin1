import random


def get_random(number=3):
    if type(number) != int:
        raise Exception("Invalid Data!")
    result = []
    while len(result) < number:
        num = random.randint(1, 100)
        if num not in result:
            result.append(num)

    result.sort()
    return result


print(get_random(5))
print(get_random())
