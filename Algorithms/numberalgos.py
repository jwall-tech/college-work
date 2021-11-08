def smallest(numbers):
    endNumb = None

    for number in numbers:
        if endNumb:
            if number < endNumb:
                endNumb = number
        else:
            endNumb = number
    return endNumb

def Search(numbers,value):
    index = 0

    for number in numbers:
        index += 1
        if number == value:
            return index

print(smallest([1,2,3,4,5]))
print(Search([1,2,5,7,78],78))
