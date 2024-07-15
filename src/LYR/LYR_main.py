import numpy as np
import matplotlib.pyplot as plt
import os
import LYR_functions as lyr
from LYR_input_parameters import *
import time


toc = time.time()

from LYR_LR_compl_part4 import *

tic = time.time()
tt = tic - toc
tt_str = 'seconds.'
if tt > 60:
	tt = tt/60
	tt_str = 'minutes.'
elif tt > 3600:
	tt = tt/3600
	tt_str = 'hours.'
print('\nComputational time:', round(tt,1), tt_str, '\n')

