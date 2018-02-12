from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import EUDistance
from mel_coefficients import mfcc
from LPC import lpc
from train import training
import os

nSpeaker = 8
#nSpeaker = 16
#nfiltbank = 12
nfiltbank = 14
orderLPC = 15
(codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)
#directory = os.getcwd() + '/traint';
directory = os.getcwd() + '/testt';
directory2 = os.getcwd() + '/testt2';
directory3 = os.getcwd() + '/testt3';
fname = str()
nCorrect_MFCC = 0
nCorrect_LPC = 0

def minDistance(features, codebooks):
    speaker = 0
    distmin = np.inf
    for k in range(np.shape(codebooks)[0]):
        D = EUDistance(features, codebooks[k,:,:])
        dist = np.sum(np.min(D, axis = 1))/(np.shape(D)[0]) 
        if dist < distmin:
            distmin = dist
            speaker = k
            
    return speaker

for i in range(0, nSpeaker):
    #fname = '/speaker' + str(i + 1) + '.wav'
    fname = '/s' + 'a' + str(i+1) + '.wav'
    print 'Now speaker ', str(i+1), 'features are being tested'
    (fs,s) = read(directory + fname)
    mel_coefs = mfcc(s,fs,nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
    
    print 'Speaker ', (i+1), ' in test matches with speaker ', (sp_mfcc+1), ' in train for training with MFCC'
    print 'Speaker ', (i+1), ' in test matches with speaker ', (sp_lpc+1), ' in train for training with LPC'
   
    if i == sp_mfcc:
        nCorrect_MFCC += 1
    if i == sp_lpc:
        nCorrect_LPC += 1

###################### PART 2 TESTING

for i in range(0, nSpeaker):
    #fname = '/speaker' + str(i + 1) + '.wav'
    fname = '/s' + 'a' + str(i+1) + '.wav'
    print 'Now speaker ', str(i + 1), 'features are being tested'
    (fs, s) = read(directory2 + fname)
    mel_coefs = mfcc(s, fs, nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)

    print 'Speaker ', (i + 1), ' in test matches with speaker ', (sp_mfcc + 1), ' in train for training with MFCC'
    print 'Speaker ', (i + 1), ' in test matches with speaker ', (sp_lpc + 1), ' in train for training with LPC'

    if i == sp_mfcc:
        nCorrect_MFCC += 1
    if i == sp_lpc:
        nCorrect_LPC += 1

###################### PART 3 TESTING
for i in range(0, nSpeaker):
    #fname = '/speaker' + str(i + 1) + '.wav'
    fname = '/s' + 'a' + str(i+1) + '.wav'
    print 'Now speaker ', str(i + 1), 'features are being tested'
    (fs, s) = read(directory3 + fname)
    mel_coefs = mfcc(s, fs, nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)

    print 'Speaker ', (i + 1), ' in test matches with speaker ', (sp_mfcc + 1), ' in train for training with MFCC'
    print 'Speaker ', (i + 1), ' in test matches with speaker ', (sp_lpc + 1), ' in train for training with LPC'

    if i == sp_mfcc:
        nCorrect_MFCC += 1
    if i == sp_lpc:
        nCorrect_LPC += 1


totalSpeakers = 16 + 8

percentageCorrect_MFCC = (nCorrect_MFCC/totalSpeakers)*100
print 'Accuracy of result for training with MFCC is ', percentageCorrect_MFCC, '%'
percentageCorrect_LPC = (nCorrect_LPC/totalSpeakers)*100
print 'Accuracy of result for training with LPC is ', percentageCorrect_LPC, '%'


    