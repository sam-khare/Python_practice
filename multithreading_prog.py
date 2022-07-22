# import time
# import threading
#
# def cal_squr(num):
#     print("calculating square of numbers")
#     for i in num:
#         time.sleep(0.2)
#         print("Square of  ",i," is:",i*i)
#
# def cal_cube(num):
#     print("calculating cube of numbers")
#     for i in num:
#         time.sleep(0.2)
#         print("cube of  ",i," is:",i*i*i)
#
# arr = [2,3,5,8,9]
# t = time.time()
# cal_squr(arr)
# cal_cube(arr)
#
# print("done in :",time.time()-t)

#########################
'''same prog with multithreading'''
# import time
# import threading
#
# def cal_squr(num):
#     #print("calculating square of numbers")
#     for i in num:
#         time.sleep(0.2)
#        # print("Square of  ",i," is:",i*i)
#
# def cal_cube(num):
#    # print("calculating cube of numbers")
#     for i in num:
#         time.sleep(0.2)
#       #  print("cube of  ",i," is:",i*i*i)
#
# arr = [2,3,5,8,9]
# t = time.time()
# t1 = threading.Thread(target=cal_squr,args=(arr,))
# t2 = threading.Thread(target=cal_cube,args=(arr,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

#print("done in :",time.time()-t)
#################multiprocessing###########
# import time
# import multiprocessing
#
# def cal_squr(num):
#     #print("calculating square of numbers")
#     for i in num:
#         time.sleep(2)
#         print("\nSquare:"+ str(i*i))
#
# def cal_cube(num):
#    # print("calculating cube of numbers")
#     for i in num:
#         time.sleep(2)
#         print("\nCube :"+ str(i*i*i))
#
# if __name__ == "__main__":
#     arr = [2,3,5,8,9]
#     p1 = multiprocessing.Process(target=cal_squr,args=(arr,))
#     p2 = multiprocessing.Process(target=cal_cube,args=(arr,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#     print("done")

############################
''' here global variable ,which is a main process variable,is not receiving any values while child variable is showing.
since child process has their own separate memory.'''
# import time
# import multiprocessing
#
# square_result = []
# def cal_squr(num):
#     #print("calculating square of numbers")
#     for i in num:
#         global square_result
#         print("\nSquare:"+ str(i*i))
#         square_result.append(i*i)
#     print("inside cal square :",square_result)
#
# if __name__ == "__main__":
#     arr = [2,3,5,8,9]
#     p1 = multiprocessing.Process(target=cal_squr,args=(arr,))
#
#
#     p1.start()
#
#
#     p1.join()
#     print("global result",square_result)
#     print("done")

############################to overcome above prob, and share data between main and child
import time
# import multiprocessing
#
#
# def cal_squr(num,result,v):
#     v.value = 3.67
#     for idx,n in enumerate(num):
#         result[idx]=n*n
#
#
#
# if __name__ == "__main__":
#     arr = [2,3,5,8,9]
#     result = multiprocessing.Array('i',5)
#     v = multiprocessing.Value('d',0.0)
#     p1 = multiprocessing.Process(target=cal_squr,args=(arr,result,v))
#     p1.start()
#     p1.join()
#    # print(v.value)
#     #print(result[:])

############using Queue
import multiprocessing


def cal_squr(num,q):

    for n in num:
        q.put(n*n)



if __name__ == "__main__":
    arr = [2,3,5,8,9]
    q = multiprocessing.Queue()
    #v = multiprocessing.Value('d',0.0)
    p1 = multiprocessing.Process(target=cal_squr,args=(arr,q))
    p1.start()
    p1.join()
    while q.empty() is False:
        print(q.get())