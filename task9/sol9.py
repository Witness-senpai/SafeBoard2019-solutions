def calc_checksum(t, l, b):
    body_sum = 0
    for el in b:
        body_sum += el

    return (int(t) + int(l) + int(body_sum)) % 8

hex_text = input()

inbytes = bytes.fromhex(hex_text)

curr_code = "utf-8"
buffer = ''
byte_num = 0
while len(inbytes) != 0:
    try:
        msg_type = inbytes[byte_num]
        body_len = inbytes[byte_num + 1]
        body_text = inbytes[byte_num + 2:byte_num + 2 + body_len]
        check_sum = inbytes[byte_num + 2 + body_len]
    except:
        break

    byte_num += body_len + 3

    if check_sum != calc_checksum(msg_type, body_len, body_text):
        continue

    if (msg_type == 1):
        try:
            buffer += body_text.decode(curr_code)
        except:
            pass
    elif (msg_type == 2):
        buffer = buffer[:-1]
    elif (msg_type == 3):
        buffer += buffer[-1]
    elif (msg_type == 4):
        if (body_text == b'\x00'): # UTF-8
            curr_code = "utf-8"
        elif (body_text == b'\x01'): # windows-1251!!!!
            curr_code = "windows-1251"
    elif (msg_type == 5): 
        print(buffer)


