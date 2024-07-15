import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import LYR_functions as lyr
from LYR_input_parameters import *


#################################################################### std deviations ########
print('Calculating std...')

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10,4))

############################################################################# output(X-ray):
err_output = np.sqrt(np.power(ra_err_output_s,2)+np.power(dec_err_output_s,2))
err_output = err_output*plus_erf*3600

entries, bin_edges, patches = ax1.hist(err_output, bins=20, color='dodgerblue', histtype='stepfilled',
									   alpha=0.7, label='Output errors', zorder=2)
bin_middles = 0.5*(bin_edges[1:] + bin_edges[:-1])
# gaussian fit method 1
parameters1, cov_matrix1 = curve_fit(lyr.gaussian, bin_middles, entries)
xgauss = np.linspace(min(err_output), max(err_output), 1000)
ygauss = lyr.gaussian(xgauss, *parameters1)

msigma_output = round(parameters1[1],2)

if sigma_out_finder == '1sigma':
	sigma_output = np.zeros(len(err_output))
	for i in range(len(err_output)):
		sigma_output[i] = msigma_output
	print('Output mean sigma:', abs(round(msigma_output,2)))
elif sigma_out_finder == 'all':
	sigma_output = err_output
	print('Using all output sigma.')

print('... done.\n')
