def big_fibonacci(n):
    if(n == 1):
        return 1
    first_prev_num = 0
    second_prev_num = 0
    cur_num = 1
    temp_num = cur_num
    while(len(str(cur_num)) != n):
        second_prev_num = first_prev_num
        first_prev_num = cur_num
        cur_num = first_prev_num + second_prev_num
    return cur_num

print(big_fibonacci(30))