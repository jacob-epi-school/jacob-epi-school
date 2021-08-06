def test_my_range(m,n):
    i = m
    final_list = []
    while(i < n):
        final_list.append(i)
        i = i+1
    return final_list


def my_range(m,n):
    result = []
    
    while m < n:
        result.append(m)
        m += 1
        
    return result
print(my_range(3,10), test_my_range(3,10))