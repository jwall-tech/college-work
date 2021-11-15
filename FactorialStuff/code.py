def factorial(number):
    if number < 0:
        return "negative error"
    elif number == 0:
        return 1
    else:
        if number-1 <= 0:
            return number
        else:
            return number * factorial(number-1)
print(factorial(5))
