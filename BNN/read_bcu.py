#
#Simple reader for .npz files in repository:
# https://github.com/manconi/agn-psr-nn-classification
#
# version 2 Dec 2021
# Tested withPython 3.6.9, numpy 1.18.4
# SM manconi@physik.rwth-aachen.de
# *

import numpy as np



#------------------------------------------
#---Reading classification results
#------------------------------------------
with np.load('predictions_bnn_bcu.npz', allow_pickle=True) as data: 
    predictions_bnn = data['predictions']
    names_bnn = data['source_names']


mean_pred_bnn=predictions_bnn.mean(0)
std_pred_bnn=predictions_bnn.std(0)


#------------------------------------------
#---Tight selection
#------------------------------------------

bll_bnn_tight=[]
fsrq_bnn_tight=[]

#filter predictions according to mean and standard deviation of BNN 
for i in range(len(names_bnn)):
	if(mean_pred_bnn[i]+std_pred_bnn[i]<0.2): 
		bll_bnn_tight.append(names_bnn[i])
	elif(mean_pred_bnn[i] - std_pred_bnn[i]>0.8): 
		fsrq_bnn_tight.append(names_bnn[i])


#------------------------------------------
#---Loose selection
#------------------------------------------
bll_bnn_loose=[]
fsrq_bnn_loose=[]

for i in range(len(names_bnn)):
	if(mean_pred_bnn[i]+std_pred_bnn[i]<0.5): 
		bll_bnn_loose.append(names_bnn[i])
	elif(mean_pred_bnn[i] - std_pred_bnn[i]>0.5): 
		fsrq_bnn_loose.append(names_bnn[i])


print('Number of FSRQ, tight selection', len(fsrq_bnn_tight))
print('Number of FSRQ, loose selection', len(fsrq_bnn_loose))

