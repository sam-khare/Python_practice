# a = [23,45,88,99]
# b = [12,76,34,90]
#
# def sum(vlist):
#     total = 0
#     for item in vlist:
#         total = total + item
#     return total
#
# sum_a = sum(a)
# sum_b = sum(b)
# final = sum_a + sum_b
# print(final)

#order/positional arguments
# def sum(a,b):
#     print("a",a)
#     print("b",b)
#     total = a +b
#     return total
#
# result = sum(5,6)
# print("sum of inputs:",result)

#named arguments
def sum(a,b):
    '''
    This function take two arguments and return their sum

    '''
    print("a",a)
    print("b",b)
    total = a +b
    return total

result = sum(a=6,b=5)

print("sum of inputs:",result)

#