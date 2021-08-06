def to_hex(x):
    d1=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    d2=[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    d3=[]
    a=0
    b=0

    while a<16:
        while b<16:
            if d1[a] == 0:
                z=str(d2[b])
            else:
                z=str(d1[a])+str(d2[b])
            d3.append(z)
            b+=1
        a+=1
        b=0

    return d3[x]

def hex_color(red,green,blue):
    r=to_hex(red)
    g=to_hex(green)
    b=to_hex(blue)
    if len(r)==1:
        r="0"+str(r)
    return "#%s"%r+g+b

print(hex_color(22,22,41),
hex_color(12,25,41),
hex_color(31,25,41))




