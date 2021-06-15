# import reverseList

# def test_my_reverse(data_list):
#     length = len(data_list)
#     s = length

#     new_list = [None]*length

#     for item in data_list:
#         s = s - 1
#         new_list[s] = item
#     return new_list

# for x in range(1000):
#     l = [x, x+1, x, x+1,x, x+1,x, x+1,x, x+1,x, x+1]
#     if(test_my_reverse(l) != reverseList.my_reverse(l)):
#         print("error")