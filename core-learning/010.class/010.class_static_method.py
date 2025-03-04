class MyCls:
    @staticmethod
    def doAdd(a,b):
        #No need to pass self
        return a+b


print(MyCls.doAdd(1,3))#4