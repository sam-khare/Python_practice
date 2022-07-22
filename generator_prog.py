# def remote_control_next():
#     yield "CNN"
#     yield "ESPN"
#
# itr = remote_control_next()
# #print(next(itr))
# #print(next(itr))
#
# for c in remote_control_next():
#     print(c)

########Fibonacci sequence using generator

def fib():
    a,b = 0,1
    while True:
        yield a
        a , b = b ,a+b

for f in fib():
    if f>100:
        break
    print(f)