def find_missing_element(arr, key):
    set_array1 = set(arr)
    set_array2 = set(key)
    diff = set_array1.difference(set_array2)


def finder_1(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


finder_1([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])

import collections

def finder2(arr1,arr2):
    d = collections.defaultdict(int)
    for num in arr2:

        d[num] += 1

    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -= 1

finder2([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])

def find_xor(arr1,arr2):
    result=0
    for num in arr1+arr2:
        result^=num
        # print(result)
    return result
print(find_xor([5,5,7,7],[5,7,7]))