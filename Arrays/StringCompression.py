def string_compress(orig):
    count = {}
    for i in orig:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key,val in count.items():
        print('{}{}'.format(key,val),end='')
    print('')

string_compress('AAB')


def compare(s):
    #Run Length Compression - Algo Name
    #Solun is Compression without Checking

    r = ''
    l = len(s)
    if l==0:
        return ''
    elif l==1:
        return s+'1'

    last = s[0]
    count = 1
    i = 1

    while i<l:
        if s[i] == s[i-1]:
            count += 1
        else:
            r = r+s[i-1]+str(count)
            count = 1
        i += 1

    r = r+s[i-1]+str(count)
    print(r)

compare('AAN')