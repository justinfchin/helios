from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import lbg
from mel_coefficients import mfcc
from LPC import lpc
import matplotlib.pyplot as plt
import os

def training(nfiltbank, orderLPC):
    nSpeaker = 8
    nCentroid = 16
    codebooks_mfcc = np.empty((nSpeaker,nfiltbank,nCentroid))
    codebooks_lpc = np.empty((nSpeaker, orderLPC, nCentroid))
    directory = os.getcwd() + '/traint3'
    fname = str()

    for i in range(0, nSpeaker):
        #fname = '/s' + str(i+1) + '.wav'
        #fname = '/s' + 'a1' + str(i + 1) + '.wav'
        #fname = '/s' + 'a2' + str(i + 1) + '.wav'
        fname = '/speaker' + str(i + 1) + '.wav'
        print 'Now speaker ', str(i+1), 'features are being trained' 
        (fs,s) = read(directory + fname)
        mel_coeff = mfcc(s, fs, nfiltbank)
        lpc_coeff = lpc(s, fs, orderLPC)
        codebooks_mfcc[i,:,:] = lbg(mel_coeff, nCentroid)
        codebooks_lpc[i,:,:] = lbg(lpc_coeff, nCentroid)

    print 'Training complete'

    return (codebooks_mfcc, codebooks_lpc)
    
    
