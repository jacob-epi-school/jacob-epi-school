def to_hex(num):
    poss_hex = "0123456789abcdef"
    hex_num = (num % 16)
    leftover = num // 16
    if(leftover == 0):
        return (poss_hex[hex_num])
    return to_hex(leftover) + poss_hex[hex_num]


def hex_color(red,green,blue):
    temp = '#'
    for item in [red,green,blue]:
        if item < 0:
            item = 0
        elif item > 255:
            item = 255
        temp += str(to_hex(item)).replace('0x','').upper().zfill(2)
    return temp