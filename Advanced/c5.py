class shape:
  def __init__(self,side):
    seld.side = side
  

  def info(self):
    return f'shape with {self.side}'

class Rectangle(Shape):

  def __init__(self, l, w):
    super().__init__(l)
    self.w = w 


  def area(self):
    return self.side * self.w   # side is taken as length


# overridden function
  def info(self):
    return f'rectangle with l = {self.side} & w = {self.w}'



ob1 = shape(4)
print(ob1.info())

ob2 = Rectangle(Shape)
print(ob2.area())
print(ob2.info)