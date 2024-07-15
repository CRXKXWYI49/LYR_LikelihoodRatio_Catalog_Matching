import matplotlib.pyplot as plt
import numpy as np
from LYR_input_parameters import *



do,di,rain,decin,magin,r,fr,df,fdf,qm,nm,lr,rel = np.genfromtxt(filename, usecols=(0,4,5,6,7,8,9,10,11,12,13,14,15), unpack=True)

fig, ax = plt.subplots(1,2, figsize=(10,4))

for i in range(len(lr)):
	ax[0].scatter(r[i], lr[i], marker='.', color='b')
	ax[1].scatter(r[i], rel[i], marker='.', color='r')

ax[0].set_yscale('log')
ax[0].set_xlabel('r [arcsec]')
ax[0].set_ylabel('LR')
ax[0].grid(ls=':', color='grey', alpha=0.4, zorder=0)
ax[1].set_xlabel('r [arcsec]')
ax[1].set_ylabel('Reliability')
ax[1].grid(ls=':', color='grey' ,alpha=0.4, zorder=0)
fig.suptitle('LR and reliability' + add_title)
ax[0].tick_params(axis='both', which='both', direction='in', top=True, right=True)
ax[1].tick_params(axis='both', which='both', direction='in', top=True, right=True)


fig, ax = plt.subplots()
for i in range(len(lr)):

	di_ = int(di[i])
	rain_ = round(rain[i],6)
	decin_ = round(decin[i],6)
	do_ = int(do[i])
	magin_ = round(magin[i],2)
	r_ = round(r[i],2)
	fr_ = round(fr[i],3)
	df_ = round(df[i],2)
	fdf_ = round(fdf[i],3)
	nm_ = round(nm[i],3)
	qm_ = round(qm[i],3)
	lr_ = round(lr[i],3)
	rel_ = round(rel[i],3)



#plt.show()
