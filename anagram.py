def check_anagram(str1,str2):
    str1=str1.replace(' ','').lower()
    str2 = str2.replace(' ', '').lower()

    s1=sorted(str1)
    s2=sorted(str2)
    return  sorted(str1)==sorted(str2)

def check_anagram2(str1,str2):

    str1=str1.replace(' ','').lower()
    str2 = str2.replace(' ', '').lower()
    if len(str1)!=len(str2):
        return False
    count = {}
    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

print(check_anagram2('dog','g o dd'))