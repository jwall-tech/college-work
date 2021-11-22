def isAnagram(string1,string2):
    letters = []
    lettersTwo = []

    for letter in string1:
        letters.append(letter)

    for letter in string2:
        lettersTwo.append(letter)
    
    for letter in string2:
        if letter in letters:
            letters.remove(letter)
            lettersTwo.remove(letter)

    if len(letters) == 0 and len(lettersTwo) == 0:
        return True
    return False

print(isAnagram("python","typhon"))
# True
print(isAnagram("python","hiya"))
# False
print(isAnagram("python","pytho"))
# False
print(isAnagram("duncan skilton","skliton ancdun"))
# True

print("\n\n\n\n")

def isAnagramTwo(string1,string2):
    letters = list(string1)
    lettersTwo = list(string2)
    
    for letter in string2:
        if letter in letters:
            letters.remove(letter)
            lettersTwo.remove(letter)

    if len(letters) == 0 and len(lettersTwo) == 0:
        return True
    return False

print(isAnagramTwo("python","typhon"))
# True
print(isAnagramTwo("python","hiya"))
# False
print(isAnagramTwo("python","pytho"))
# False
print(isAnagramTwo("duncan skilton","skliton ancdun"))
# True
