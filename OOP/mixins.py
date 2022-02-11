class Demo:
    def __init__(self):
        self.field = 'abc'
        self.field2 = 'bnb'
        

    def fields_count(self):
        return len(self.__dict__.keys())


d = Demo()
print(d.fields_count())
