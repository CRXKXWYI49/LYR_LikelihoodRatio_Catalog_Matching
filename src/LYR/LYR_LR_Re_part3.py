import numpy as np
import matplotlib.pyplot as plt

import LYR_functions as lyr
from LYR_input_parameters import *
from LYR_distrib_part2 import *



############################################################# LR and Reliability ###
print('LR and Reliability:')

neigh_idx_lr = tree.query_ball_point(r_out_tree, r=r_lr)

d=0
for i in range(len(neigh_idx_lr)):
	for j in range(len(neigh_idx_lr[i])):
		rain_tmp = r_in_tree[neigh_idx_lr[i],0]
		decin_tmp = r_in_tree[neigh_idx_lr[i],1]
		Dra_tmp = (r_out_tree[i,0] - rain_tmp[j])
		Ddec_tmp = (r_out_tree[i,1] - decin_tmp[j])
		rr_lr = lyr.quadratic_sum(Dra_tmp, Ddec_tmp)
		if rr_lr <= r_lr:
			d=d+1
	prog = 100*i/len(ID_output)
	print ('Counting sources: '+str(int(prog)+1)+'%', end="\r")

lr_inRA = np.zeros(d)
lr_inDEC = np.zeros(d)
lr_outRA = np.zeros(d)
lr_outDEC = np.zeros(d)
lr_mag_in = np.zeros(d)
lr_LR = np.zeros(d)
lr_inID = np.zeros(d)
lr_outID = np.zeros(d)
lr_r = np.zeros(d)
lr_flux_output = np.zeros(d)
lr_fluxerr_output = np.zeros(d)
lr_flux_input = np.zeros(d)
lr_fluxerr_input = np.zeros(d)
rel = []
lr_noID = []
flag = []
fr_r_tmp = np.zeros(d)
fr_fr_tmp = np.zeros(d)
fdf_delta_tmp = np.zeros(d)
fdf_fdf_tmp = np.ones(d)
nnm_ = np.zeros(d)
qm_ = np.zeros(d)

d=0
for i in range(len(neigh_idx_lr)):
	lr_singleXID = []
	for j in range(len(neigh_idx_lr[i])):
		rain_tmp = r_in_tree[neigh_idx_lr[i],0]
		decin_tmp = r_in_tree[neigh_idx_lr[i],1]
		Dra_tmp = (r_out_tree[i,0] - rain_tmp[j])
		Ddec_tmp = (r_out_tree[i,1] - decin_tmp[j])
		rr_lr = lyr.quadratic_sum(Dra_tmp, Ddec_tmp)
		if rr_lr <= r_lr:
			ra_tmp = ra_input[neigh_idx_lr[i]]
			lr_inRA[d] = ra_tmp[j]
			dec_tmp = dec_input[neigh_idx_lr[i]]
			lr_inDEC[d] = dec_tmp[j]
			mag_tmp = mag_input[neigh_idx_lr[i]]
			lr_mag_in[d] = mag_tmp[j]
			inID_tmp = ID_input[neigh_idx_lr[i]]
			lr_inID[d] = inID_tmp[j]
			lr_outID[d] = ID_output[i]
			lr_outRA[d] = ra_output[i]
			lr_outDEC[d] = dec_output[i]
			lr_r[d] = rr_lr


			#calcolo la LR(fr,nm,qm) per ogni sorgente

			if delta_f2 == False:

				lr_flux_output[d] = 0.
				lr_fluxerr_output[d] = 0.
				lr_flux_input[d] = 0.

				if (input_cat_type == 2) or (input_cat_type == 0):
					fr_r_tmp[d], fr_fr_tmp[d] = lyr.FR(sigma_output[i],sigma_input,Dra_tmp,Ddec_tmp)
					nnm_[d] = nnm_interp(lr_mag_in[d])
					qm_[d] = qm_interp(lr_mag_in[d])
					lr_LR[d] = lyr.LR(fr_fr_tmp[d],nnm_[d],qm_[d])
				elif input_cat_type == 1:
					sigma_in_tmp = sigma_input[neigh_idx_lr[i]]
					fr_r_tmp[d], fr_fr_tmp[d] = lyr.FR(sigma_output[i],sigma_in_tmp[j],Dra_tmp,Ddec_tmp)
					nnm_[d] = nnm_interp(lr_mag_in[d])
					qm_[d] = qm_interp(lr_mag_in[d])
					lr_LR[d] = lyr.LR(fr_fr_tmp[d],nnm_[d],qm_[d])

			#... e memorizzo quelle della singola XID temporaneamente:
			lr_singleXID = np.append(lr_singleXID, lr_LR[d])
			d=d+1

	#calcolo Re con le LR nell'intorno delle singole XID:
	if len(lr_singleXID) != 0.:
		summLR = np.sum(lr_singleXID)
		single_outID_LR = []
		rel_sum_tmp = []
		for k in range(len(lr_singleXID)):
			rel_tmp = lyr.Re(summLR, lr_singleXID[k], Q)
			rel = np.append(rel, rel_tmp)
			#rel_sum_tmp = np.append(rel_sum_tmp, rel_tmp)
			single_outID_LR = np.append(single_outID_LR, lr_singleXID[k])
		# find the maximum likelihood of each output source (1 == max LR; 0 == non max LR):
		LR_max_tmp = max(single_outID_LR)
		#rel_sum = np.append(rel_sum, np.sum(rel_sum_tmp))
		for ff in range(len(single_outID_LR)):
			if single_outID_LR[ff] < LR_max_tmp:
				flag_tmp = 0
				flag = np.append(flag, flag_tmp)
			elif single_outID_LR[ff] == LR_max_tmp:
				flag_tmp = 1
				flag = np.append(flag, flag_tmp)
	else:
		lr_noID = np.append(lr_noID, ID_output[i])
	prog = 100*i/len(ID_output)
	print ('Filling array: '+str(int(prog)+1)+'%', end="\r")




non_matched=len(lr_noID)/len(ID_output)
print('Unmatched',len(lr_noID),'sources (',int(100*non_matched)+1,'%):\n', lr_noID)

