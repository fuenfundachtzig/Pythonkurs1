#!/usr/bin/env python3

import random

dice1 = [random.randrange(1,7) for i in range(1,10) ]
dice2 = [ (random.randrange(1,7),random.randrange(1,7)) for i in range(1,10) ]

print(dice1)
print(dice2)
