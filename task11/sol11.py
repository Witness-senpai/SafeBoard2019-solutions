def code_from_country(country):
    if (country == 'RUR'):
        return '810'
    elif (country == 'EUR'):
        return '978'
    elif (country == 'USD'):
        return '840'
    elif (country == 'GBP'):
        return '826'

def num_from_days(days):
    if (days <= 30):
        return '42302'
    elif (31 <= days <= 90):
        return '42303'
    elif (91 <= days <= 180):
        return '42304'
    elif (181 <= days <= 365):
        return '42305'
    elif (365 <= days <= 365*3):
        return '42306'
    else:
        return '42307'

def get_key(BIK, tbill):
    num_org = BIK[-3:]
    temp_bill = num_org + tbill

    mul_list = []
    for e1, e2 in zip(temp_bill, '71371371371371371371371'):
        mul_list.append(str(int(e1) * int(e2)))
    
    res = 0
    for el in mul_list:
        res += int(el[-1])

    return (res * 3) % 10      

def generate_bill(s):
    days, country, BIK, num = s.split(' ')

    temp_bill = num_from_days(int(days)) + \
                code_from_country(country) + \
                '00000' + num

    key = get_key(BIK, temp_bill)

    bill = temp_bill[:-12] + str(key) + temp_bill[-11:]

    return bill

s = input()

print(generate_bill(s))

