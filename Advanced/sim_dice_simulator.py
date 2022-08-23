import random

while True: 
  input('Enter to roll dice ') # fake input to simulate user input
  roll = random.randint(1, 6)
  print('you rolled dice and got: ',roll)
  if roll == 1:
    print('lose!')
    break
  elif roll == 6:
    print('You won!')
    break
  else:
    print('Keep rolling...')
    