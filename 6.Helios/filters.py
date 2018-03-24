'''
Authors : Justin Chin
Purpose:
    List of Filters
'''

import scipy.signal as s # for filters
import scipy.io.wavfile as wav # for reading wav files
import numpy as np

def wiener(filename,newFilename):
    """
    Args:
        filename : string
            filename of the wav file without the .wav
        newFilename : string
            newFilename without the .wav
    Returns:
        saves a .wav file post filtering in same folder
        prints message
    """
    
    # pull data from original
    fs,data = wav.read(filename+'.wav')
    # perform the filter
    data = s.wiener(data)
    # convert the datatype back to np.in16
    data = data.astype(np.int16)
    # saves the new wavfile
    wav.write(newFilename+'.wav',fs,data)
    # print message
    print(newFilename+'.wav saved')
