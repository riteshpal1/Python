''' wap to create a class Movie that have 
properties like
-title
-rating
-year
then create a constructor and a function to 
display the info, Also create 5 movie object,
store them in a list them in a list then sort 
them by rating'''

class movie:
  title = 'Jab tak hai jaan'
  rating = '4.8'
  year = '2016'


  def info(self):
    return f'movie with {self.title}'
    return f'movie with {self.rating}'
    return f'movie with {self.year}'

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