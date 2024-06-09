# rand(): generate random value between 0 and 1

# randn(): generate random value close to 0

# ranf(): generate random value close to [0.0, 1.0]

# randint(): generate random number between 0 and 1

import numpy as np

var = np.random.rand(4)
var

var = np.random.rand(4)
var

var = np.random.randn(4)
var

min = 4
max = 90
tot_val = 5
var = np.random.randint(min, max, tot_val)
var
