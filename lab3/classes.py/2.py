class Shape:
    def __init__(self):
        pass
    def area (self):
        print(0)  # по умолчанию площадь фигуры = 0
class Square(Shape): 
    def __init__(self, length): 
        self.length=length 
    def area(self):
        print(self.length*self.length)
p = Square(int(input()))
p.area()