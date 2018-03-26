from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import lbg
from LPC import lpc
from python_speech_features import mfcc as mfcc_p
import matplotlib.pyplot as plt
import os


"""We train the model using 16 speakers, 8 male voices and 8 female voices.
The input given is still the combination of LINE1 plus LINE2."""

def training(nfiltbank, orderLPC):

    #Get directory and list of *.wav files
    directory = os.getcwd() + '/train_all_speakers'
    wave_files = [f for f in os.listdir(directory)]

    nSpeaker = len(wave_files)
    nCentroid = 32  # original is 16
    codebooks_mfcc = np.empty((nSpeaker, nfiltbank, nCentroid))
    codebooks_lpc = np.empty((nSpeaker, orderLPC, nCentroid))

    for i, wave_file in enumerate(wave_files):
        fname = '/' + wave_file
        print 'Speaker [' + str(i) + ']    File:' + wave_file + '    Training features...'
        (fs, s) = read(directory + fname)
        mel_coeff = mfcc_p(s, fs)
        mel_coeff = mel_coeff.transpose()
        mel_coeff[0, :] = np.zeros(mel_coeff.shape[1])

        lpc_coeff = lpc(s, fs, orderLPC)
        codebooks_mfcc[i, :, :] = lbg(mel_coeff, nCentroid)
        codebooks_lpc[i, :, :] = lbg(lpc_coeff, nCentroid)

    print('Training finished\n')

    return (codebooks_mfcc, codebooks_lpc)


