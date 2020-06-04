''' Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of heads and tails. '''

import random

while True:
    try:
        numFlips = int(input("How many time would you like to flip the coin? "))
        break
    except ValueError:
        print("Invalid value! Please enter a number!")
        
heads_tails = []
heads = 0
tails = 0

for i in range(numFlips):
    coin = random.randint(0, 1)
    if coin == 0:
        heads_tails.append("T")
        tails += 1
    else:
        heads_tails.append("H")
        heads += 1
        
print(heads_tails)
print("Number of heads:", heads)
print("Number of tails:", tails)