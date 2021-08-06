def test_my_reverse(in_list):
    out_list = []
    j = len(in_list) - 1
    while(j >= 0):
        out_list.append(in_list[j])
        j = j-1
    return out_list

def my_reverse(list):
    return list[::-1]

for x in range(1000):
    l = [x, x+1, x, x+1,x, x+1,x, x+1,x, x+1,x, x+1]
    if(test_my_reverse(l) != my_reverse(l)):
        print("error")