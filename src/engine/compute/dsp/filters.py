from scipy.signal import butter, lfilter



def butterworth(lowcut, highcut, fs, order=5):
    """
    Function for applying butterworth filter to a signal.

    Wiki: The Butterworth filter is a type of signal processing filter designed to have a frequency response
            as flat as possible in the passband. It is also referred to as a maximally flat magnitude filter.

    :param lowcut:
    :param highcut:
    :param fs:
    :param order:
    :return:
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a, c = butter(order, [low, high], btype='band')
    return b, a
