def isUnique(orig):
    return len(orig) == set(orig)


def isUnique2(orig):
    chars = set()
    for i in orig:
        if i in chars:
            return False
        else:
            chars.add(i)
    return True


print(isUnique2('abcde'))
