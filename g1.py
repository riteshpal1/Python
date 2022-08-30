
import pgzrun

WIDTH = 800
HEIGHT = 400

box = Rect((50,150), (50,100))
box2 = Rect((105,150),(50,50))


def draw():
  screen.fill('yellow')
  screen.draw.text('hola amigos',(50,50), color='red', fontsize=30)
  screen.draw.text('this is a game programming',(50,80), color='blue',fontsize=50)
  screen.draw.rect(box, color='black')
  screen.draw.filled_rect(box2,color='brown')
def update():
  box.x += 1
  box2.y += 2


pgzrun.go()