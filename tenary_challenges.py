def one():
    x = 0
    x = "even" if x % 2 == 0 else "false"
    print(x)

def two():
    mark = 90

    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    else:
        grade = "C"

    print(grade)

def three():
    bill = 10000

    discount = bill * 10.0/100 if bill >= 1000 else bill * 5.0/100

    print(discount)

one()
two()
three()
