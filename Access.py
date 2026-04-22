class Student:
    def __init__(self,A,B,C): # parameterised const
        self.Name = A # public
        self._Age = B # protected
        self.__Marks = C # private
    
    def Display(self):
        print(self.Name)
        print(self._Age)
        print(self.__Marks)

obj = Student('Rahul',24,89)
obj.Display()

print(obj.Name)
print(obj._Age)
#print(obj.__Marks)
#print(obj._Student.__Marks)