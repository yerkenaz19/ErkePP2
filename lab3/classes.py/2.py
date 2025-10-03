# class Shape:
#     def __init__(self):
#         pass
#     def area (self):
#         print(0)  # по умолчанию площадь фигуры = 0
# class Square(Shape): 
#     def __init__(self, length): 
#         self.length=length 
#     def area(self):
#         print(self.length*self.length)
# p = Square(int(input()))
# p.area()

class Circle:
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        print(2*3.14*self.radius**2)
    def perimetr(self):
        print(2*3.14*self.radius)
p=Circle(int(input()))
p.area()
p.perimetr()