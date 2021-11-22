import math
global ind
ind = 0
def binarySearch(dataset,target):
    mini = 0
    maxi = len(dataset)
    found = False
    
    def s1(maxi,mini):
        global ind
        ind += 1
        if ind == 500:
            return 0
        if maxi < mini:
            return -1
        print(maxi,mini)
        avrg = math.floor((maxi-mini)/2)
        
        print(avrg)
        
        if dataset[avrg] == target:
            return avrg
        elif dataset[avrg] < target:
            mini = avrg+1
        else:
            maxi = avrg -1
        return s1(maxi,mini)

    return s1(maxi,mini)

binarySearch([x for x in range(25)],25)
