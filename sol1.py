
data = []
best_ = [0,0,0]
while True:
    try:
        s = input()
        if s != '\n':
            data.append(s.split(' '))
        else:
            break
    except:
        break


for el1 in data:
    for el2 in data:
        s1 = el1[0].split(':')
        s2 = el2[0].split(':')
        if int(el2[1]) - int(el1[1]) > best_[2] and (int(s1[0])*60 + int(s1[1]) <= int(s2[0])*60 + int(s2[1])):
            best_[0] = el1[0]
            best_[1] = el2[0]
            best_[2] = int(el2[1]) - int(el1[1])
print(f"{best_[0]} {best_[1]} {best_[2]}")

