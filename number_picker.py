import random


def generated_numbers_pb():
    main_numbers = random.sample(range(1, 69), 5)
    main_numbers.sort()
    money_ball = random.randint(1, 26)
    numbers = ','.join(map(str, main_numbers)) + f',{money_ball}'
    return numbers


def generated_numbers_mega():
    main_numbers = random.sample(range(1, 70), 5)
    main_numbers.sort()
    money_ball = random.randint(1, 25)
    numbers = ','.join(map(str, main_numbers)) + f',{money_ball}'
    return numbers