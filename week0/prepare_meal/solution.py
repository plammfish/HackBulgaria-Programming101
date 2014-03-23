def prepare_meal(number):
    result = ""

    if prepare_meal_spam(number) and prepare_meal_eggs(number):
        result = prepare_meal_spam(number) + " and " + \
        prepare_meal_eggs(number)
    else:
        if prepare_meal_spam(number):
            result = prepare_meal_spam(number)
        else:
            result = prepare_meal_eggs(number)

    return result

def prepare_meal_spam(number):
    counter = 0
    while number % 3 == 0:
        counter += 1
        number = number / 3
    if counter != 0:
        return " ". join(["spam"] * counter)
    else:
        return ""


def prepare_meal_eggs(number):
    if number % 5 == 0:
        return "eggs"
    return ""


