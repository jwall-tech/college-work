def list_xor(n,list1,list2):
    if n in list1 and not n in list2:
        return True

    if n in list2 and not n in list1:
        return True

    return False

print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
