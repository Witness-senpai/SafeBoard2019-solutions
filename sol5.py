def find_pair(data, curr, pair):
    for el in data:
        if el[0] == pair[0]:
            return find_pair(data, (el[1], pair[1]))
        if el == pair:
            return el

pairs = []
while True:
    try:
        s = input()
        pairs.append(s.split(' '))
    except:
        break

q = pairs[-1]

print(find_pair(pairs[:-1], pairs[-1][0], pairs[-1]))
