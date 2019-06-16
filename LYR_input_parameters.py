############################
### LYR input parameters ###
############################

import numpy as np
print('\n')
print('Reading catalogues and parameters..')


# f(r) searching radius:
r_fr = 5 # in arcsec
# total(m) searching radius:
r_in_tm = 2 # in arcsec
# LR searching radius for FR
r_lr = 5 #in arcsec

# n(m) annulus searching annulus:
r_min_nm = 5   # in arcsec
r_max_nm = 30

# distributions bins:
distrib_bins = 21

# results:
path_LR = '/Users/Alessandro/Documents/post_TESI/codes/LYR/'
path_output = path_LR + 'output/'
path_images = path_LR + 'images/'

# output catalogue errors moltiplicative factor
plus_erf = 1 # wavdetect errors factor, put 1 if there isn't

# sigma finder ('all' == every single source; '1sigma' == 1 sigma mean errror):
sigma_out_finder = 'all'

# input catalog type(0 = static pos. error (put 0 below is there are no errors); 1 = usual errors;  2 = two catalogue with no errors):
input_cat_type = 2

# catalogues parameters:
noxy = -99. # coords of undetected sources
nomag = -99. # mag/fluxes of undetected sources

# use of fluxes of IO catalogue:
delta_f2 = False
delta_f2_fluxerr = 0 # 0: static error; 1: every single error for the input cat

# python interactions
iwp = True
cursors = False
save_images = True
save_output = True

# sdding string to all output images
add_str = 'Final_XJ'
# adding string to images titles
add_title = add_str

# out catalog and info
filename_LR = 'LR_' + add_str + '.txt'
filename_outinfo = 'LR_outinfo_' + add_str + '.txt'


############################################################### import data ########
# coordinates in degrees

######################################################################################################## ONIR - X:
# Input catalogue:
#file_input = "/Users/Alessandro/Documents/post_TESI/J1030/catalogues/original/J1030_match_new99.txt" #z: 0,1,2,3
#file_input = "/Users/Alessandro/Documents/post_TESI/J1030/catalogues/original/1030_Catalog_r_indip_deep.txt" #r: 0,3,4,7
file_input = "/Users/Alessandro/Documents/post_TESI/J1030/catalogues/original/SDSSJ1030_J_catalog.txt" #J: 0,1,2,7


data_input = np.genfromtxt(file_input)
ID_input = np.array(data_input[:,0])
ra_input = np.array(data_input[:,1])
dec_input = np.array(data_input[:,2])
mag_input = np.array(data_input[:,7])


# Output catalogue:
#file_output = "/Users/Alessandro/Documents/post_TESI/codes/LYR/new_err/new_Xerr_ONIR_wd.txt" # 0,1,2,4,5
file_output = "/Users/Alessandro/Documents/post_TESI/codes/LYR/Catalogs/final_catalog_X_LR.txt" # 0,1,2,3,4


data_output = np.genfromtxt(file_output)
ID_output = np.array(data_output[:,0])
ra_output = np.array(data_output[:,1])
dec_output = np.array(data_output[:,2])
ra_err_output = np.array(data_output[:,4])
dec_err_output = np.array(data_output[:,5])

#file_output_err = "/Users/Alessandro/Documents/post_TESI/codes/LYR/new_err/new_Xerr_ONIR.txt"
#data_output_err = np.genfromtxt(file_output_err)
#ra_err_output = np.array(data_output_err[:,3])
#dec_err_output = np.array(data_output_err[:,3])

#---------------------------------------------------------------------- for sigma selection ------

# Sigma input (ONIR):
file1 = "/Users/Alessandro/Documents/post_TESI/J1030/catalogues/J1030_match_new99+J1030_j_cat.txt"
data1 = np.genfromtxt(file1)
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
#file2 = "/Users/Alessandro/Documents/post_TESI/J1030/catalogues/chandra_catalog_4s_rizYJ_v3.1.txt"
#data2 = np.genfromtxt(file2)
ID_output_s = ID_output
ra_output_s = ra_output
dec_output_s = dec_output
ra_err_output_s = ra_err_output
dec_err_output_s = dec_err_output

'''
######################################################################################################### Xi - Xo:
# Catalogo input:
file_input = "/Users/Alessandro/Documents/post_TESI/codes/LYR/XIO_catalogues/input_hard_2.txt"
data_input = np.genfromtxt(file_input)
ID_input = np.array(data_input[:,0])
ra_input = np.array(data_input[:,1])
dec_input = np.array(data_input[:,2])
mag_input = np.log10(np.array(data_input[:,3]))

if delta_f2_fluxerr == 0:
	magerr_input = 0 # if != 0 put the error in log10 with (np.log10(magerr_input))
elif delta_f2_fluxerr == 1:
	magerr_input = np.log10(np.array(data_input[:,3]))


# Catalogo output:
#file_output = "/Users/Alessandro/Documents/post_TESI/codes/LYR/new_err/new_Xerr_XIO_probnosrc.txt"
file_output = "/Users/Alessandro/Documents/post_TESI/codes/LYR/new_err/Xerr_output_hard_2.txt"
data_output = np.genfromtxt(file_output)
ID_output = np.array(data_output[:,0])
ra_output = np.array(data_output[:,1])
dec_output = np.array(data_output[:,2])
ra_err_output = np.array(data_output[:,4])
dec_err_output = np.array(data_output[:,5])
if delta_f2 == True:
	flux_output = np.log10(np.array(data_output[:,8]))
	fluxerr_output = np.log10(np.array(data_output[:,9]))
	#pnos = (1-np.array(data_output[:,10]))

#flux_output = np.log10(np.array(data_output[:,8]))
#fluxerr_output = np.log10(np.array(data_output[:,9]))


#---------------------------------------------------------------------- for sigma selection ------

# Sigma input:
file1 = file_input
data1 = np.genfromtxt(file1)
ID1_input_s = np.array(data1[:,0])
ra1_input_s = np.array(data1[:,1])
dec1_input_s = np.array(data1[:,2])
mag1_input_s = np.log10(np.array(data1[:,3]))


if input_cat_type == 0:
	sigma_input = 0

elif input_cat_type == 1:
	ra1_input_s_err = np.array(data1[:,30])
	dec1_input_s_err = np.array(data1[:,30])

elif input_cat_type == 2:
	ID2_input_s = np.array(data1[:,34])
	ra2_input_s = np.array(data1[:,35])
	dec2_input_s = np.array(data1[:,36])



# Sigma output:
#file2 = "/Users/Alessandro/Documents/post_TESI/J1030/catalogues/chandra_catalog_4s_rizYJ_v3.1.txt"
#data2 = np.genfromtxt(file2)
ID_output_s = ID_output
ra_output_s = ra_output
dec_output_s = dec_output
ra_err_output_s = ra_err_output
dec_err_output_s = dec_err_output
if delta_f2 == True:
	flux_output_s = flux_output
	fluxerr_output_s = fluxerr_output
'''


print('... done.\n')
