import array as arr

a = arr.array("i",[5,6,1,2,3])

i = 0

while i < 3:
    print(a[i])
    i += 1

rev = arr.array("i",reversed(a))

print(rev)

leng = len(a)

def findDupes(a):
    numberOc = {}


    for ib in range(0,len(a)-1):
        b = a[ib]
        
        try:
            numberOc[b] += 1
        except:
            numberOc[b] = 1

    return numberOc


a2 = arr.array("i",[5,5,5,6,7,4,2,2,2,2])

dupes = findDupes(a2)

def remFromInd(a,ind):
    try:
        a.remove(a[ind])
    except:
        return

print(dupes)

print(a2)
remFromInd(a2,1)
print(a2)

