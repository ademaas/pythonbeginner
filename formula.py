import math

class Formula:
    def __init__(self):
        self.d = []
        self.c = ''
        self.h = ''
        self.value = []

    def getElement(self):
        self.c= 50
        self.h = 30
        self.d = [x for x in input().split(',')]

    def calculating_value(self):
        
        for x in (self.d):
            q= math.sqrt((2*self.c*int(x))/self.h)
            self.value.append(q)
        print(self.value)

    def print_result(self):
        self.calculating_value()


formulaobj = Formula()
formulaobj.getElement()
formulaobj.print_result()

    