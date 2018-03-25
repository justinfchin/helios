"""
Authors : Justin Chin
Purpose:
    List of Filters
"""

import scipy.signal as s            # for filters
import scipy.io.wavfile as wav      # for reading wav files
import numpy as np


def wiener(nd_array):
    """
    Apply Wiener Filter to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """
    fil = s.wiener(nd_array)
    return fil


def butter(nd_array):
    """
    Apply Butterworth Filter with predefined parameters
    to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """
    N = "<class 'numpy.int16'>"
    b, a = s.butter(20, .3, 'low', analog=False)
    # Apply the filter for a single channel
    if str(type(nd_array[0])) == N:
        fil = s.filtfilt(b, a, nd_array, method='gust')
        return fil
    # Apply the filter for 2 Channels
    else:
        fil = s.filtfilt(b, a, nd_array.T[0], method='gust')
        return fil


def cheby1(nd_array):
    """
    Apply Chebyshev Type I Filter with predefined parameters
    to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """
    N = "<class 'numpy.int16'>"
    b, a = s.cheby1(20, 2, .3, 'lowpass', analog=False, output='ba')
    # Apply the filter for a single channel
    if str(type(nd_array[0])) == N:
        fil = s.filtfilt(b, a, nd_array, method='gust')
        return fil
    # Apply the filter for 2 Channels
    else:
        fil = s.filtfilt(b, a, nd_array.T[0], method='gust')
        return fil


def filter_and_save(filter_func, directory, filename):
    """
    Filter the WAV file located at the directory by converting it to numpy array
    and then passing the array into a filtering function. The transformed
    numpy array is then converted back into WAV file and stored in the
    specified storage directory

    :param filter_func: A function that takes one argument of numpy array object
    :param directory: Directory where the filtered data will reside
    :param filename: An input WAV file that is going to be filtered
    :return: A string containing the relative location of the filtered WAV file in the disk
    """

    storage_dir = './static/results/' \
                  + filename.rsplit('.', 1)[0].lower() \
                  + '_' + filter_func.__name__ + '.wav'

    # Convert the WAV file into numpy array with a specified sample rate
    rate, nd_array = wav.read(directory + filename)

    # Pass the numpy array into a filtering function and store the result
    result = filter_func(nd_array)

    # Convert the output numpy array back into WAV file
    data = result.astype(np.int16)

    # Write the output into the disk at the specified directory and sample rate
    wav.write(storage_dir, rate, data)

    return storage_dir
