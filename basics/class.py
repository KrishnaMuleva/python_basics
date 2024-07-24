class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def MyFunc(self):
        print("my name is:"+self.name+ "and my age is:"+self.age)
p1=MyClass('bert','20')
p1.MyFunc()
