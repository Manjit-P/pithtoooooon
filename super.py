from abc import ABC ,abstractmethod
class shape(ABC):

    def __init__(self, is_filled):
        self.is_filled = is_filled
    
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, is_filled, radius):
        super().__init__(is_filled)
        self.radius = radius
    def area (self) -> float:
        return 3.14*self.radius ** 2

class triangle(shape):
    def __init__(self,is_filled, base, height):
        super().__init__(is_filled)
        self.base = base
        self.height = height
    def area(self) -> float:
        return 0.5*self.base*self.height


tri = triangle(True, 3, 9)
cir = circle( False, 7)
print(tri.area())
print(cir.area())