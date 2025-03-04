class MyCls:
    _result=None
    @property
    def result(self):
        #This is propery result
        return self._result

    @result.setter
    def result(self,v):
        self._result=v




obj=MyCls()
obj.result='hello'
print(obj.result)#Result