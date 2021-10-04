for integer in range(1,50):
    if integer % 3:
        print("Fizz")
        if integer % 5:
            print("FizzBuzz")
    elif integer % 5:
        print("Buzz")
