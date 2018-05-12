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

    fil = s.wiener(nd_array).astype(np.int16)
    return fil


def butter(nd_array):
    """
    Apply Butterworth Filter with predefined parameters
    to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """

    N = "<class 'numpy.int16'>"
    b, a = s.butter(20, .3, 'low', analog=False)#our defult values
    if (str(type(nd_array[0])) == N):
        filtered = s.filtfilt(b, a, nd_array, method='gust')#applying the filter for single channel
    else:
        filtered = s.filtfilt(b, a, nd_array.T[0], method='gust')#applying the filter 2 channels

    # Cast the array to int16 type
    fil = filtered.astype(np.int16)
    return fil


def cheby1(nd_array):
    """
    Apply Chebyshev Type I Filter with predefined parameters
    to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """

    N = "<class 'numpy.int16'>"
    b, a = s.cheby1(20, 3, .3, 'low',analog= False, output='ba')#our defult values
    if (str(type(nd_array[0])) == N):
        filtered = s.filtfilt(b, a, nd_array, method='gust')#applying the filter
    else:
        filtered = s.filtfilt(b, a, nd_array.T[0], method='gust')#applying the filter

    # Cast the array to int16 type
    fil = filtered.astype(np.int16)
    return fil


def cheby_butter(nd_array):
    """
    Apply Cheby Type I Filter followed by Butter Filter
    to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """

    return butter(cheby1(nd_array))


def butter_cheby(nd_array):
    """
    Apply Butter Filter followed by Chebyshev Type I Filter 
    to the input numpy array

    :param nd_array: Array of data to be filtered
    :return: Filtered output with the same shape as nd_array
    """

    return cheby1(butter(nd_array))


def apply_n_times(filter_name, nd_array, iteration=1):
    """
    Apply a filter to the input nd_array repeatedly
    as determined by the iteration parameter

    :param filter_name: The filter function to be applied
    :param nd_array: Array of data to be filtered
    :param iteration: Number of times the filter will be applied
    :return: Filtered output with the same shape as nd_array
    """

    for _ in range(iteration):
        nd_array = filter_name(nd_array)

    return nd_array


def filter_and_save(filter_func, directory, filename, iteration=1):
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
                  + '_' + filter_func.__name__ \
                  + '_' + str(iteration) + 'n.wav'

    # Convert the WAV file into numpy array with a specified sample rate
    rate, nd_array = wav.read(directory + filename)

    # Pass the numpy array into a filtering function and store the result
    result = apply_n_times(filter_func, nd_array, iteration)

    # Convert the array into WAV file and write the output 
    # into the disk at the specified directory and sample rate
    wav.write(storage_dir, rate, result)

    return storage_dir
