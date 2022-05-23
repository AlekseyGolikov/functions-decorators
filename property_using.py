from msilib.schema import Property


class Person(object):
    
    def __init__(self):
        self.__name = ''
    
    @property
    def setname(self, name):
        print(f"{self.setname.__name__} is called")
        self.__name = name
    
    @property
    def getname(self):
        print(f"{self.getname.__name__} is called")
        return self.__name

    @property
    def delname(self):
        print(f"{self.delname.__name__} is called")
        del self.__name
    # name = property(getname, setname, delname)

