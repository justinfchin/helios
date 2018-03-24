'''
Authors : Justin Chin
Purpose:
    List of Filters
'''

import scipy.signal as s # for filters
import scipy.io.wavfile as wav # for reading wav files
import numpy as np


def wiener(dir, filename):
    # pull data from original
    fs, data = wav.read(dir + filename)
    # perform the filter
    data = s.wiener(data)
    # convert the datatype back to np.in16
    data = data.astype(np.int16)
    # saves the new wavfile
    # wav.write(newFilename+'.wav',fs,data)
    file_loc = './static/results/' + filename.rsplit('.', 1)[0].lower() + '_wiener.wav'
    wav.write(file_loc, fs, data)
    # print message
    # print(newFilename+'.wav saved')
    return file_loc
