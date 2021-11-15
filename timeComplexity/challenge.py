
cards = [10,8,6,4,3,1,0,2,6,1,2,4,5,1,2,45,6,7,3,5,5,1,15,6]

def find(tab,my,turns=0):
    turns = turns or 0
    mid = round(len(tab)/2)

    midInd = mid - 1

    midVal = tab[midInd]
    turns += 1

    if len(tab) == 2:
        turns += 1

        return turns
    
    if midVal == my:
        return turns;
    elif midVal > my:
        return find(tab[midInd:],my,turns=turns)
    else:
        return find(tab[:midInd],my,turns=turns)

t = find(cards,10)
print(t)
