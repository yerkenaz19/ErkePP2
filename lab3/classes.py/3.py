class Shape: #родительский класс
    def area(self):
        print(0) # по умолчанию возвращает 0, посколько форма (shape) может быть разной (круг,прямоугольник)
class Rectangle(Shape): #дочерный класс
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width
        
    def area(self):
        print(self.length*self.width)
        
rectangle=Rectangle(5,2)
rectangle.area()