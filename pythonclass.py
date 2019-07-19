class Sample:
    def __init__(self):
        self.s = ""

    def getstring(self):
        self.s = input('Enter a new astring: ')

    def printToUppercae(self):
        print(self.s.upper())

classobje = Sample()
classobje.getstring()
classobje.printToUppercae()


