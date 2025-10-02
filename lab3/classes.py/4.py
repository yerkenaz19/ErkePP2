class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
        
    def move(self):
        self.t=self.y # временная перемена t используется для хранение y 
        self.y=self.x
        self.x=self.t
        print(self.x, self.y)
    def dist(self):
        print(abs(self.x-self.y))

p=Point(7,12)
p.show()
p.move()
p.dist()