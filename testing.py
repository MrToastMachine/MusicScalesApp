class Test():
    allStuff = []
    def __init__(self, x):
        # print("init")
        self.x = x
        Test.allStuff.append(self)
    
    @classmethod
    def allThings(cls):
        for i in cls.allStuff:
            print(i.x)


class newTest(Test):
    # pass
    def __init__(self, x):
        Test.__init__(self,x)
        
    def printVals(self):
        print(self.x)

t = newTest(5)
t.printVals()