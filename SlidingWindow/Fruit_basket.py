def totalFruit(fruits):
    
    left = 0
    max_count = 0
    sett = set()

    for right in range(len(fruits)):
        sett.add(fruits[right])

        if len(sett) > 2:
            sett.remove(fruits[left])
            left += 1
        
        max_count = max(max_count, right-left+1)
    return max_count

fruits = [1,2,1]
print(totalFruit(fruits))
fruits = [0,1,2,2]
print(totalFruit(fruits))
fruits = [1,2,3,2,2]
print(totalFruit(fruits))
#and fruits[right] not in sett: