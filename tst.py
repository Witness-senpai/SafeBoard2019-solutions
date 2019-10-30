def calc_checksum(t, l, b):
    body_sum = 0
    for el in b:
        body_sum += el

    return (int(t) + int(l) + int(body_sum)) % 8

hex_text = input()

curr_code = "utf-8"
buffer = ''
byte_num = 0
while len(inbytes) != 0:
    msg_type = hex_text[byte_num: byte_num + 2]
    body_len = hex_text[byte_num + 2: byte_num + 4]
    body_text = hex_text[byte_num + 2:byte_num + 2 + body_len]
    check_sum = hex_text[byte_num + 3 + body_len + 1]
    # inbytes = inbytes[:2 + body_len + 1]

    byte_num += body_len + 4

    #if check_sum != calc_checksum(msg_type, body_len, body_text):
    #    continue

    if (msg_type == 1):
        buffer += body_text.decode(curr_code)
    elif (msg_type == 2):
        buffer = buffer[:-1]
    elif (msg_type == 3):
        buffer += buffer[-1]
    elif (msg_type == 4):
        if (body_text == 0): # UTF-8
            curr_code == "utf-8"
        elif (body_text == 1): # ASCII
            curr_code == "ascii-8"
    elif (msg_type == 5): 
        print(buffer)


