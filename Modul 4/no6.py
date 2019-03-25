def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) - 1
    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            return "target di index "+str(mid)
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

list = [2,4,5,7,33,45,46,65,76]
target = 33
print(binSe(list,target))
list = [2,4,5,7,33,45,46,65,76]
target = 27
print(binSe(list,target))
