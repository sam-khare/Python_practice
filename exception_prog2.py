# try:
#     raise MemoryError('My Memory Error')
# except MemoryError as e:
#     print(e)
#
# try:
#     raise Exception('generic exception')
# except Exception as e:
#     print(e)

#User Defined Exception derived from Exception class
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        1/0
        print("user defined exception:",self.msg)

try:
    raise Accident("crash between two cars")
except Accident as e:
    e.print_exception()
finally:
    print("I am gonna run no matter what")