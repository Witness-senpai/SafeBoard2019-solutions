import string

alphabet = string.ascii_lowercase

code = input()

def correct(code):
    for el in alphabet:
        if (el + el.upper()) in code or (el.upper() + el) in code:
            return False
    
    return True

def del_gen(code, gen):
    new_code = code.replace(gen, '').replace(gen.upper(), '')

    while (not correct(new_code)):
        for g in alphabet:
            new_code = new_code.replace(g + g.upper(), '').replace(g.upper() + g, '')

    return len(new_code)

def find_min_len(code):
    lens = []
    for gen in alphabet:
        lens.append(del_gen(code, gen))
    
    return min(lens)

print(find_min_len(code))

