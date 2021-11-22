def binary(lis,target,defaultListVal=0):
    maxi,mini = len(lis),0

    if target > defaultListVal or target < 0:
        return None

    

    average = round((mini-maxi)/2)


    if lis[average] == target:
        return True

    if lis[average] < target:
        mini = average -1

    if lis[average] > target:
        maxi = average + 1
        
    return binary(lis[mini:maxi],target,defaultListVal=defaultListVal)

tab = [x for x in range(1000)]
print(binary(tab,501,defaultListVal=len(tab)))
