def test_to_hex(num):
    poss_hex = "0123456789abcdef"
    hex_num = (num % 16)
    leftover = num // 16
    if(leftover == 0):
        return (poss_hex[hex_num])
    return test_to_hex(leftover) + poss_hex[hex_num]


def test_hex_color(red,green,blue):
    temp = '#'
    for item in [red,green,blue]:
        if item < 0:
            item = 0
        elif item > 255:
            item = 255
        temp += str(test_to_hex(item)).replace('0x','').upper().zfill(2)
    return temp

  
def to_hex(n):
    if (n < 0):
        return 0
    elif (n<=1):
     return n 
    else:
        to_hex ( n / 16 )
        x =(n%16)
        if (x < 10):
            print(x), 
        if (x == 10):
            print("A"),
        if (x == 11):
            print("B"),
        if (x == 12):
            print("C"),
        if (x == 13):
            print("D"),
        if (x == 14):
            print("E"),
        if (x == 15):
            print ("F")

def hex_color(r, g, b):
  return  ('{:X}{:X}{:X}').format(r, g, b)

print(hex_color(10,32,255))

# print(to_hex(255))
print(test_hex_color(10,32,255))


# for i in range(0,100):
#     if(to_hex(i) != test_to_hex(i)):
#         print("error: ", i)