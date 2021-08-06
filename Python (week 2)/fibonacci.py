def test_big_fibonacci(n):
    if(n == 1):
        return 1
    first_prev_num = 0
    second_prev_num = 0
    cur_num = 1
    while(len(str(cur_num)) != n):
        second_prev_num = first_prev_num
        first_prev_num = cur_num
        cur_num = first_prev_num + second_prev_num
    return cur_num


def big_fibonacci(n):
    if n < 0:
        return None
    num1 = 1
    num2 = 1
    while len(str(num1)) < n:
        keep = num1
        num1 += num2
        num2 = keep
    return num1

       
for i in range(1,100):
    if(big_fibonacci(i)!=test_big_fibonacci(i)):
        print("Error at: ",i, big_fibonacci(i), test_big_fibonacci(i))