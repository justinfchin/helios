'''
Title: Functions to run other 
Author 1: Justin Chin
Author 2: Sunny Mei

How to use: from process import `function`
Or: import process as `p`
'''

'''########## PACKAGES ##########'''
# Import necessary packages
import scipy.io as sio  # for importing matlab file
import matplotlib.pyplot as plt # for plotting
import scipy.io.wavfile as wav # for saving as .wav file
import numpy as np  
import os   # for opening file
import math # for log calculations
import matlab # for matlab functions

'''########## FILE MANIPULATION ##########'''
# Loads matlab data into a variable
def load(matlabfile):
   """
   Parameters
   ----------
   matlabfile : str
    the matlab filename

   Returns
   -------
   data : numpy array
    the matlab data
   """
   matdata = sio.loadmat(matlabfile) # a dictionary
   data = matdata['data']   # get value associated with keyword in dictionary
   return data

#normal plotting function
#takes in data we want to plot, name of the file
#saves it as a png file
def plot(data, filename):
    plt.figure(figsize=(20,10))##change the size of the charts
    plt.plot(data)
    plt.show()
    #iplt.savefig(filename+".png",bbox_inches='tight')

# Saves data as a .wav file
def save_wav(data, filename):
    """
    Parameters
    ----------
    data : array
        the data to be saved as .wav
    filename : str
        file name of the new .wav 
    """
    wav.write(filename+".wav", 44100, ((data + data.min()) * (2 ** 15) / data.ptp()).astype(np.int16))

# Opens the file indicated by filename
def play(filename):
    """
    Parameters
    ----------
    filename : str
        the file to be opened
    """
    
    os.system("open "+filename)

'''########## SIGNAL PROCESSING ##########'''
# SNR
# Note: that scipy.stats.signaltonoise is defined as mean divided by standard deviation which is usually for images. 
    # we want S/N = 20 log10(Asignal/Anoise)
### MAKE SURE THIS IS CORRECT
def snr(array):
    """
    Parameters
    ----------
    array : array
        matlab data
    Returns
    -------
    snr in dB (decibels)
    """
    
    mean = np.mean(array)
    sd = np.std(array)
    snr = mean/sd

    return 10*math.log(snr,10)  # returns dB


'''########## TESTING ###########'''
# delete this afterwards
if __name__ == '__main__':
    print("HIII")
