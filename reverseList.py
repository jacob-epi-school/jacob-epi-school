def my_reverse(in_list):
    out_list = []
    j = len(in_list) - 1
    while(j >= 0):
        out_list.append(in_list[j])
        j = j-1
    return out_list
