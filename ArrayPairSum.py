def pair_sum(arr,key):
    myset=set()
    for i in arr:
        for j in arr:
            if i+j==key and (i,j) not in myset and (j,i) not in myset:
                myset.add((i,j))
    return len(myset)

print(pair_sum([1,3,2,2], 4))


def pair_sum_O(arr,key):
    if len(arr)<2:
        return

    seen = set()
    output = set()
    for num in arr:
        target = key-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target,num),max(target,num)))
    return output




print(pair_sum_O([1, 3, 2, 2], 4))