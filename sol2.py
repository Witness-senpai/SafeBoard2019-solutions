data = []
while True:
    try:
        s = input()
        if s != '':
            data.append(s.split(":")[1].replace(' ', ''))
        else:
            break
    except:
        break

mysum = 0
for el in data:
    mysum += int(el)

avr =  mysum / float(len(data))
defects = 0
for el in data:
    if (abs(int(el) - avr) > (avr * 0.1)):
        defects += 1

print(defects)



