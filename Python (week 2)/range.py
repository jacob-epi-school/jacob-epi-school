def my_range(m,n):
    i = m
    final_list = []
    while(i < n):
        final_list.append(i)
        i = i+1
    return final_list

print(my_range(3,10))