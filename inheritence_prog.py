# class Vehicle:
#     def general_usage(self):
#         print("general use : transportation")
#
# class Car(Vehicle):
#     def __init__(self):
#         print("I am a car")
#         self.wheels = 4
#         self.has_roof = True
#
#     def specific_usage(self):
#         print("specific usage: commute to work, vacation with family")
#
# class MotorCycle(Vehicle):
#     def __init__(self):
#         print("I am a motorcycle")
#         self.wheels = 2
#         self.has_roof = None
#
#     def specific_usage(self):
#         self.general_usage()
#         print("specific usage: road trip, racing")
#
# c = Car()
# #c.general_usage()
# #c.specific_usage()
#
# m = MotorCycle()
# #m.specific_usage()
# print(isinstance(c,Car))
# print(issubclass(Car,Vehicle))

######################Multiple Inheritance##########

# class Father():
#     def gardening(self):
#         print("I enjoy gardening")
# class Mother():
#     def cooking(self):
#         print("I love cooking")
# class Child(Father,Mother):
#     def sports(self):
#         print("I love playing sports")
#
# ch = Child()
# ch.sports()
# ch.cooking()
# ch.gardening()

######
class Father():
    def skills(self):
        print("programmer,gardening")
class Mother():
    def skills(self):
        print("cooking,arts")
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")
c = Child()
c.skills()