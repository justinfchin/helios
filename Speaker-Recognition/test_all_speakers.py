from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import EUDistance
from python_speech_features import mfcc as mfcc_p
from LPC import lpc
from train_all_speakers import training
import os

"""Testing

The test perform here uses Random Lines with words never heard before
from the 16 trained speakers.
"""

#Start training on speakers. Call training file function
nfiltbank = 13  # was 12
orderLPC = 15
(codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)

#Get files for testing
directory = os.getcwd() + '/test_all_speakers'
wave_files = [f for f in os.listdir(directory)]
nSpeaker = len(wave_files)

#Counters for accuracy
nCorrect_MFCC = 0
nCorrect_LPC = 0


def minDistance(features, codebooks):
    speaker = 0
    distmin = np.inf
    for k in range(np.shape(codebooks)[0]):
        D = EUDistance(features, codebooks[k, :, :])
        dist = np.sum(np.min(D, axis=1)) / (np.shape(D)[0])
        #print "DISTANCE!!!" + str(dist)
        if dist < distmin:
            distmin = dist
            speaker = k

    return speaker

print "|||||STARTING TEST|||||\n"

for i,wave_file in enumerate(wave_files):
    fname = '/' + wave_file
    to_print = 'Speaker ['+ str(i) + ']   File:' + wave_file + '    Testing features...'
    print to_print
    (fs, s) = read(directory + fname)

    #Passing test file to MFCC
    mel_coefs = mfcc_p(s, fs)
    mel_coefs = mel_coefs.transpose()
    mel_coefs[0, :] = np.zeros(mel_coefs.shape[1])  # 0th coefficient does not carry significant information

    #Passing test file to LPC
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)

    print 'Speaker [' + str(i) + '] matches Speaker ['+ str(sp_mfcc) + ']   ||MFCC||'
    print 'Speaker [' + str(i) + '] matches Speaker ['+ str(sp_lpc) + ']    ||LPC||\n'

    if i == sp_mfcc:
        nCorrect_MFCC += 1
    if i == sp_lpc:
        nCorrect_LPC += 1

percentageCorrect_MFCC = (nCorrect_MFCC / nSpeaker) * 100
print 'MFCC Accuracy: '+ str(percentageCorrect_MFCC) + '%'
percentageCorrect_LPC = (nCorrect_LPC / nSpeaker) * 100
print 'LPC Accuracy:' + str(percentageCorrect_LPC) + '%\n'