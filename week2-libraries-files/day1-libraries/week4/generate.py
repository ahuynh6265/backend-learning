#from week 4 cs50p 

import random

coin = random.choice(['heads', 'tails'])

number = random.randint(1,10)

cards = ['jack', 'queen', 'king']
random.shuffle(cards)

for card in cards:
  print(card)





'''
from random import choice

coin = choice(['heads', 'tails'])
print(coin)
'''