strings = []
while True:
    try:
        s = input()
        if s != '':
            strings.append(s)
        else:
            break
    except:
        break

def check(strings):
    for str1 in strings:
        for str2 in strings:
            if (str1 == str2):
                continue
            count = 0
            n = 0
            num = 0
            for el1, el2, in zip(str1, str2):
                if (el1 != el2):
                    count += 1
                    num = n
                    if count >= 2:
                        break
                n += 1
            
            if (count == 1):
                return (str1[:num] + str1[num + 1:])
                
print(check(strings))