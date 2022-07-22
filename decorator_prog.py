import time
# def calc_squares(numbers):
#     start = time.time()
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     end = time.time()
#     print("total time to run squares:",str((end-start)*1000)+"mil sec")
#     return result
#
#
# def calc_cubes(numbers):
#     start = time.time()
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     end = time.time()
#     print("total time to run cubes:", str((end - start) * 1000) + "mil sec")
#     return result
#
# array = range(1,100000)
# out_squ = calc_squares(array)
# out_cube = calc_cubes(array)

###########################same operation with decorator##########
# def time_it(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(func.__name__ + " took "+ str((end-start)*1000)+" mil sec ")
#         #return result
#     return wrapper
#
# @time_it
# def calc_squares(numbers):
#
#     result = []
#     for number in numbers:
#         result.append(number*number)
#
#     return result
#
# @time_it
# def calc_cubes(numbers):
#
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#
#     return result
#
# array = range(1,100000)
# out_squ = calc_squares(array)
# out_cube = calc_cubes(array)
#############################################
'''Decorators are a very powerful and useful tool in Python since it allows programmers
 to modify the behaviour of a function or class. Decorators
  allow us to wrap another function in order to extend the behaviour of the wrapped function,
   without permanently modifying it.
In Python, functions are first class objects which means that 
   functions in Python can be used or passed as arguments.
'''
'''function trated as objects'''
def shout(text):
    return text.upper()
#print(shout("Hello"))

yell = shout("Yell hello")
#print(yell)

'''functions passed as an arguments to other functions'''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("I am created by a function passed as an argument")
    #print(greeting)

greet(shout)
greet(whisper)
#########################
# Python program to illustrate functions
# Functions can return another function

def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func

out_f = outer_func(10)
inner_f = out_f(20)
#print(inner_f)

######################
'''
As stated above the decorators are used to modify the behaviour of function or class. 
In Decorators, functions are taken as the argument into another function and
 then called inside the wrapper function.
'''

def hello_decorator(func):
    def inner1():
        print("this is before function execution")
        func()
        print("this is after function execution")
    return inner1


def func_pass():
    print("I am inside the passed funciton")

var_func = hello_decorator(func_pass)
var_func()

##########Factorial time
import time,math

def cal_time(func):
    def inner1(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("total time taken",func.__name__,end-begin)
    return inner1
@cal_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)