from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(Module.get_title(title))
        self.grades[self.modules[0]] = Module.get_grade(title)

    def get_list_modules(self):
        for m in self.modules:
            print ("Module of Student {0:s}: \n".format(self.name),m)

    def get_grades(self):
        for g in self.grades.items():
            print("Grades of Student {0:s}: \n".format(self.name),g)


### test cases ###

me = Student("Vera Isler")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
