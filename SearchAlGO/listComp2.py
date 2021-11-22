string = "Practice Problems to Drill List Comprehension in Your Head."

def NumbOfSpaces(string):
    return len(string.split(" "))

def RemVowles(string):
    vowels = ["a","e","i","o","u"]

    newString = ""

    for letter in string:
        if not (letter.lower() in vowels):
            newString += letter

    return newString

def LessThan(string,inte):
    words = []
    for word in string.split(" "):
        if len(word) <= inte:
            words.append(word)
    return words

lis = [x for y in range(2,9) for x in range(1000) if x%y == 0]

print(NumbOfSpaces(string))
print("\n\n")
print(RemVowles(string))
print("\n\n")
print(LessThan(string,5))
print("\n\n")
print(lis)
