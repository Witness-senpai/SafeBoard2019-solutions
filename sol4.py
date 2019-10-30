with open('dataset_267210_1.txt', "r", encoding='utf-8') as f:
    all_text = f.read().splitlines()

last = {}
lines = ''

for num, line in enumerate(all_text):
    try:
        sec = line.split(' ')[0]
        thread = line.split(' ')[1]
    except Exception as ex:
        print(str(ex) + " " + line + " " + str(num)) 
    temp = last.get(thread)
    if (not temp is None):
        try:
            h,m,s = last.get(thread)[0].split(':')
            last_sec = int(h) * 60 + int(m) * 60 + int(s)
            h,m,s = sec.split(':')
            new_sec = int(h) * 60 + int(m) * 60 + int(s)
            if (new_sec - last_sec) > 3:
                lines += last.get(thread)[1] + ' '
            last.update({thread:(sec, str(num + 1))})
        except:
            print(f"{last_sec} {new_sec} {thread} {line}")
    else:
        last.update({thread:(sec, str(num + 1))})

    
print(lines)