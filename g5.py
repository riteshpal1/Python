import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 500

# actor
p = Actor('aman', (50, 200))
c = Actor('fish', (randint(0, WIDTH), randint(0, HEIGHT) ))
#e = Actor('fish1', (randint(500, WIDTH), randint(500, HEIGHT) ))


speed = 3 # speed of movement
score = 0 # global variable

def draw():
  screen.fill('black')
  p.draw()
  screen.draw.text(f'score: {score}' ,(600,460), color='red', fontsize=25)
  c.draw()
 # e.draw()

def update():
  player_controls()
  check_score()

def c_movement():

  if p.x > WIDTH:
    p.x = 0
  if c.y > HEIGHT:
    c.y = 0
  if c.y < 0:
    c.y = HEIGHT
  if p.x < 0:
    p.x = WIDTH

def check_score():
  global score
  if p.colliderect(c):
    score+= 10
    c.pos = (randint(0, WIDTH), randint(0, HEIGHT) )
    sounds.s1.play()

def player_controls():
  if keyboard.UP and not p.top < 0:
    p.y += -speed
    p.angle = 0
  elif keyboard.DOWN and not p.bottom > HEIGHT:
    p.y += speed
    p.angle = 0
  elif keyboard.LEFT and not p.left < 0:
    p.x += -speed
    p.angle = 10
  elif keyboard.RIGHT and not p.right > WIDTH:
    p.x += speed
    p.angle = -10
  else:
    p.angle = 0

pgzrun.go()