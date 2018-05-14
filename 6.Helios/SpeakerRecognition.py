from __future__ import division
import numpy as np
from scipy.io.wavfile import read
from LBG import *
from LPC import lpc
from python_speech_features import mfcc
import os

def training(nfiltbank,orderLPC):
    """Train the speaker recognition model
    using .wav files from the Speaker folder.
    Feature extraction is done in two ways:
    MFCC and LPC

    Parameters
    ----------
    nfiltbank: number of filter banks for mfcc (default 13)
    orderLPC: number or order for LPC (default 15)

    Return
    ------
    Returns a pair (codebooks_mfcc, codebooks_lpc)
    which are the encoded clusters for trained speakers"""



    # Get directory and list of speaker *.wav files
    original_dir = os.getcwd()
    directory = os.getcwd() + '/static/speakers'

    os.chdir(directory)
    wave_files = filter(os.path.isfile, os.listdir(directory + "/"))
    wave_files = [os.path.join(directory, f) for f in wave_files]  # add path to each file
    wave_files.sort(key=lambda x: os.path.getmtime(x))

    os.chdir(original_dir)

    def cutDirectoryFromName(file):
        if os.name == 'nt':
            for i,c in enumerate(file):
                if file[-(i+1)] == "\\":
                    return file[-(i):]
        else:
            for i,c in enumerate(file):
                if file[-(i+1)] == "/":
                    return file[-(i):]

    wave_files = list(map(lambda x: cutDirectoryFromName(x),wave_files))

    nSpeaker = len(wave_files)
    nCentroid = 32  # original is 16
    codebooks_mfcc = np.empty((nSpeaker, nfiltbank, nCentroid))
    codebooks_lpc = np.empty((nSpeaker, orderLPC, nCentroid))

    for i, wave_file in enumerate(wave_files):
        fname = '/' + wave_file
        (fs, s) = read(directory + fname)

        mel_coeff = mfcc(s, fs)
        mel_coeff = mel_coeff.transpose()
        mel_coeff[0, :] = np.zeros(mel_coeff.shape[1])

        lpc_coeff = lpc(s, fs, orderLPC)
        codebooks_mfcc[i, :, :] = lbg(mel_coeff, nCentroid)
        codebooks_lpc[i, :, :] = lbg(lpc_coeff, nCentroid)

    print('Training finished\n')

    return (codebooks_mfcc, codebooks_lpc)

def add_new_speaker(new_name):
    """Adds new speaker to text file

    Paremeters
    ----------
    name: name of the speaker for future reference"""

    # At this point the new speaker should be in
    # the Speakers folder

    #Add new name to textfile
    file = open("Speaker_Names.txt", "a")
    file.write(new_name + '\n')
    file.close()


def recognize_speaker(codebooks_mfcc, codebooks_lpc, wav):
    """
    Predicts speaker for .wav file using trained clusters

    Parameters
    ---------
    codebooks_mfcc: trained clusters for MFCC
    codebooks_lpc: trained clusters for LPC

    Returns
    -------
    A pair of strings for the speaker prediction of both methods MFCC and LPC

    """

    def minDistance(features, codebooks):
        speaker = 0
        distmin = np.inf
        for k in range(np.shape(codebooks)[0]):
            D = EUDistance(features, codebooks[k, :, :])
            dist = np.sum(np.min(D, axis=1)) / (np.shape(D)[0])
            # print "DISTANCE!!!" + str(dist)
            if dist < distmin:
                distmin = dist
                speaker = k

        return speaker

    #Read .wave file
    (fs, s) = read(wav)

    # Passing test file to MFCC
    mel_coefs = mfcc(s, fs)
    mel_coefs = mel_coefs.transpose()
    mel_coefs[0, :] = np.zeros(mel_coefs.shape[1])  # 0th coefficient does not carry significant information

    # Passing test file to LPC
    lpc_coefs = lpc(s, fs, 15)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)

    #Find the speaker stored in the textfile
    with open("Speaker_Names.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    speaker_names = [x.strip() for x in content]

    return ("You are " + speaker_names[sp_mfcc] + '\n', "You are " + speaker_names[sp_lpc] + '\n')
