l1 = []
for i in range(1000):
    l1.append(i)

l2 = [x for x in range(1000)]

l3 = [x for x in range(1000) if x % 8 == 0]

l4 = [x for x in range(1000) if "6" in list(str(x))]
print(l1)
print("\n\n")
print(l2)
print("\n\n")
print(l3)
print("\n\n")
print(l4)
