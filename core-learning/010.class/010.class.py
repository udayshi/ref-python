class ParentCls:
    def __init__(self,a,b):
        self.a = a
        self.b=b

    def parentCalculate(self):
        return self.a+self.b



class ChildClass(ParentCls):
    def __init__(self,a,b,c):
    
        ParentCls.__init__(self,a,b)
        self.c=c

        # or
        #super().__init__(a,b)

    def __str__(self):
        return 'Value of a: {},b: {} and C: {}'.format(self.a, self.b, self.c)

    def __repr__(self):
        return 'obj=ClildClass({},{},{})'.format(self.a, self.b, self.c)


a=ParentCls(1,2)
print(a.parentCalculate()) #3

b=ChildClass(1,2,3)
print(b.parentCalculate())#3