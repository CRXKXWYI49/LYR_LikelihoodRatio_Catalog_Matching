############################
### LYR input parameters ###
############################

import numpy as np
print('Reading catalogues and parameters..')


# f(r) searching radius:
r_fr = 8 # in arcsec
# total(m) searching radius:
r_in_tm = 3 # in arcsec
# LR searching radius for FR
r_lr = 8 #in arcsec

# n(m) annulus searching annulus:
r_min_nm = 10   # in arcsec
r_max_nm = 20

# distributions bins:
distrib_bins = 21

# output catalogue errors moltiplicative factor
plus_erf = 1 # wavdetect errors factor, put 1 if there isn't

# sigma finder ('all' == everwy single source; '1sigma' == 1 sigma mean errror):
sigma_out_finder = '1sigma'

# input catalog type(0 = static pos. error (put 0 below is there are no errors); 1 = usual errors;  2 = two catalogue with no errors):
input_cat_type = 0

# catalogues parameters:
noxy = -99. # coords of undetected sources
nomag = -99. # mag/fluxes of undetected sources

# use of fluxes of IO catalogue:
delta_f2 = False
delta_f2_fluxerr = 0 # 0: static error; 1: every single error for the input cat

# python interactions
iwp = True



############################################################### import data ########
# coordinates in degrees

######################################################################################################## ONIR - X:
# Input catalogue:
file_input = "/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/data/edff_LYR.txt"

data_input = np.genfromtxt(file_input, delimiter=',')
ID_input = np.array(data_input[:,0])
ra_input = np.array(data_input[:,1])
dec_input = np.array(data_input[:,2])
mag_input = np.array(data_input[:,3])


# Output catalogue:
file_output = "/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/data/erass_LYR.txt"


data_output = np.genfromtxt(file_output, delimiter=',')
ID_output = np.array(data_output[:,0])
ra_output = np.array(data_output[:,1])
dec_output = np.array(data_output[:,2])
ra_err_output = np.array(data_output[:,3])
dec_err_output = np.array(data_output[:,4])


#---------------------------------------------------------------------- for sigma selection ------

# Sigma input (ONIR):
file1 = "/Users/admin/Documents/GitHub/LYR_LikelihoodRatio_Catalog_Matching/src/data/edff_LYR.txt"
data1 = np.genfromtxt(file1, delimiter=',')
ID1_input_s = np.array(data1[:,0])
ra1_input_s = np.array(data1[:,1])
dec1_input_s = np.array(data1[:,2])
mag1_input_s = np.array(data1[:,3])

if input_cat_type == 0:
	sigma_input = 0 # 0.3 per cosmos

elif input_cat_type == 1:
	ra1_input_s_err = np.array(data1[:,30])
	dec1_input_s_err = np.array(data1[:,30])

elif input_cat_type == 2:
	mag2_input_s = np.array(data1[:,30])
	ID2_input_s = np.array(data1[:,34])
	ra2_input_s = np.array(data1[:,35])
	dec2_input_s = np.array(data1[:,36])


# Sigma output (X-ray):
ID_output_s = ID_output
ra_output_s = ra_output
dec_output_s = dec_output
ra_err_output_s = ra_err_output
dec_err_output_s = dec_err_output



print('... done.\n')
