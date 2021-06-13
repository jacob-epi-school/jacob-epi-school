def to_hex(num):
    poss_hex = "0123456789abcdef"
    hex_num = (num % 16)
    leftover = num // 16
    if(leftover == 0):
        return (poss_hex[hex_num])
    return to_hex(leftover) + poss_hex[hex_num]


def hex_color(red,green,blue):
    final_string = "#" + to_hex(red) + to_hex(green) + to_hex(blue)
    return final_string


print(hex_color(10,32,255))