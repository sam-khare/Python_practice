#1/0 #Zero division error
#'abc'+2 #cannot concatnate string with int
# x = input("enter numerator: ")
# y = input("Enter denominator: ")
# z = None
# try:
#     z = int(x)/int (y)
# except Exception as e:
#     print("Exception occured: ",e)
# print("Division is :",z)

############
x = input("enter numerator: ")
y = input("Enter denominator: ")
z = None
try:
    z = x/int (y)
except ZeroDivisionError:
    print("Division by zero exception")
except Exception as e:
    print("exception type:",type(e).__name__)
print("Division is :",z)