# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a
# string from the user and print_string prints the string in reverse order 

class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
