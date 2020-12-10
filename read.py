#
#Simple reader for .npz files in repository:
# https://github.com/manconi/agn-psr-nn-classification
#
# version 9 Dec 2020
# Tested withPython 3.6.9, numpy 1.18.4
# SM manconi@physik.rwth-aachen.de
# *


import numpy as np


#------------------------------------------
#-------Guide to filenames
#------------------------------------------
#Results for: architectures using both energy and time spectra and GLAT for YNG vs MSP
dnn_filename= 'DNN_both_LAT_classifications.npz'
rnn_filename= 'RNN_both_LAT_classifications.npz'

#Result for: architectures using energy spectra and GLAT for YNG vs MSP
#dnn_filename= 'DNN_LAT_classifications.npz'
#rnn_filename= 'RNN_LAT_classifications.npz'

#Result for: architectures using energy spectra only
#dnn_filename= 'DNN_classifications.npz'
#rnn_filename= 'RNN_classifications.npz'

#------------------------------------------
#------------------------------------------
#------------------------------------------


#------------------------------------------
#---Reading classification results
#------------------------------------------
with np.load(dnn_filename, allow_pickle=True) as data:
    agn_dnn = data['agn']
    psr_dnn = data['psr']
    msp_dnn = data['msp']
    yng_dnn = data['yng']

with np.load(rnn_filename, allow_pickle=True) as data:
    agn_rnn = data['agn']
    psr_rnn = data['psr']
    msp_rnn = data['msp']
    yng_rnn = data['yng']


print('DNN MSP list', msp_dnn)
print('RNN MSP list', msp_rnn)


