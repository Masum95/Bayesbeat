import numpy as np
import heartpy as hp

from scipy.signal import resample
import sys
from sklearn.preprocessing import scale
from sklearn.preprocessing import minmax_scale
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime
import pandas as pd
import os

# Commented out IPython magic to ensure Python compatibility.
# %%capture
#
# !wget https://c.ndtvimg.com/2020-08/1cvf367_yellow-cat_625x300_25_August_20.jpg -O p1.jpg
# !wget https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/close-up-of-cat-wearing-sunglasses-while-sitting-royalty-free-image-1571755145.jpg -O p2.jpg
from Bayesbeat import settings

sample_rate = 10


def Layer_1(raw, windowsize, overlap=0):
    mx = np.max(raw)
    mn = np.min(raw)
    global_range = mx - mn

    # windowsize = 300
    # filtered = []
    final_filtered_data = []
    end = 0
    i = 0

    while (end + windowsize) <= len(raw):
        start = int((i * windowsize) - (overlap * windowsize * i))
        end = int(start + windowsize)
        i = i + 1
        # #print('Range ', i, ': ')
        # #print('Start :', start)
        # #print('End :', end)
        sliced = raw[start:end]
        rng = np.max(sliced) - np.min(sliced)

        if ((rng >= (0.5 * global_range))
                or
                (np.max(sliced) >= 0.9 * mx)
                or
                (np.min(sliced) <= mn)):

            print('Rejected!')
            # for x in sliced:
            #    filtered.append(0)
        else:
            #print('Accepted!')
            filtered = []
            for x in sliced:
                filtered.append(x)
            final_filtered_data.append(filtered)
        # filtered.clear()
        # #print('\n')

    return final_filtered_data


def Layer_1_mod(raw, windowsize, overlap=0, cutoff_val=2500000):
    mx = np.max(raw)
    mn = np.min(raw)
    global_range = mx - mn

    # windowsize = 300
    # filtered = []
    final_filtered_data = []
    end = 0
    i = 0

    while (end + windowsize) <= len(raw):
        start = int((i * windowsize) - (overlap * windowsize * i))
        end = int(start + windowsize)
        i = i + 1
        #print('Range ', i, ': ')
        #print('Start :', start)
        #print('End :', end)
        sliced = raw[start:end]
        max_val = np.max(sliced)

        if max_val >= cutoff_val:

            print('Rejected!')
            # for x in sliced:
            #    filtered.append(0)
        else:
            #print('Accepted!')
            filtered = []
            for x in sliced:
                filtered.append(x)
            final_filtered_data.append(filtered)
        # filtered.clear()
        #print('\n')
    return final_filtered_data


# Passing through a Band-pass filter (0.5Hz - 4.00Hz) / (30bpm -240 bpm)

def Layer_2(layer1_output, minFreq=0.5, maxFreq=4.00, sample_rate=10.00):
    layer2_output = np.empty([len(layer1_output), len(layer1_output[0])])
    for i in range(len(layer1_output)):
        band_filtered = hp.filter_signal(np.array(layer1_output[i]), [minFreq, maxFreq], sample_rate=sample_rate,
                                         order=3, filtertype='bandpass')
        layer2_output[i] = band_filtered
    return layer2_output


# Resample the signal (increase frequency)
# using freq_enhancer_factor = 10
def Layer_3(layer2_output, freq_enhancer_factor=3.2, sample_rate=10.00):
    layer3_output = []
    for i in range(layer2_output.shape[0]):
        resampled_sig = resample(layer2_output[i], int(len(layer2_output[i]) * freq_enhancer_factor))
        layer3_output.append(resampled_sig)
    new_sample_rate = sample_rate * freq_enhancer_factor
    return (layer3_output, new_sample_rate)


# Segments are eliminated those hertpy can’t process due to ‘bad signal warning’
# Handled with try-except
# Returns the working_data too for later peak analysis
def Layer_4(layer3_output, new_sample_rate):
    layer4_output = []
    reject = 0
    wd_list = []
    for i in range(len(layer3_output)):
        # #print(i)
        try:
            wd, m = hp.process(np.array(layer3_output[i]), sample_rate=new_sample_rate, bpmmin=30, bpmmax=240)
            layer4_output.append(layer3_output[i])
            wd_list.append(wd['binary_peaklist'])
            # hp.plotter(wd, m)
        except:
            # #print('HeartPy couldn\'t process')
            reject = reject + 1
    #print('Rejection Percentage: ', (reject * 100.00) / len(layer3_output))
    return (layer4_output, wd_list)


def Layer_5(layer4_output, wd_list, peak_acceptance_cutoff=0.7):
    layer5_output = []
    for i in range(len(layer4_output)):
        ratio = np.count_nonzero(wd_list[i] == 1) / (len(wd_list[i]))
        #print(i, ': ', ratio)
        if (ratio >= peak_acceptance_cutoff):
            layer5_output.append(layer4_output[i])
    return layer5_output


# Downsample to desired new_freq (32Hz) + divide in segments of desired duration (25sec)
# Standardize [0,1] the signal

def Layer_6(layer5_output, freq=32, sec=25, new_sample_rate=100.00):
    layer6_output = []
    length = freq * sec
    new_freq = (length * new_sample_rate) / (len(layer5_output[0]))
    for i in range(len(layer5_output)):
        resampled = resample(np.array(layer5_output[i]), int(len(layer5_output[i]) * new_freq / new_sample_rate))
        for j in range(len(resampled) // length):
            start = j * length
            end = (j + 1) * length
            # norm = np.linalg.norm(resampled)
            # normal_arr = resampled / norm
            # layer6_output.append(normal_arr)
            # #print(resampled[start:end])
            resampled_scaled = minmax_scale(resampled[start:end], feature_range=(0, 1), axis=0, copy=False)
            # #print(resampled_scaled)
            layer6_output.append(resampled_scaled)

    fin_layer6_output = np.array(layer6_output)
    return (fin_layer6_output, new_freq)


def preprocess_bayesbeat(raw, sample_rate=10):
    layer1_output = Layer_1(raw, 250, 0.6)
    layer2_output = Layer_2(layer1_output)
    layer3_output, new_sample_rate = Layer_3(layer2_output, freq_enhancer_factor=3.2,
                                             sample_rate=sample_rate)
    layer4_output, wd_list = Layer_4(layer3_output, new_sample_rate)
    layer5_output = Layer_5(layer4_output, wd_list, 0.3)
    layer6_output, new_freq = Layer_6(layer5_output, new_sample_rate=new_sample_rate)
    final_output = np.reshape(np.copy(layer6_output), (layer6_output.shape[0], layer6_output.shape[1], 1))
    return final_output, layer6_output, new_freq


def processed_sig_from_file(file_path):
    df = pd.read_csv(file_path)
    raw = df.values[:, 1]
    return preprocess_bayesbeat(raw)


def pdf_generate(filename: str, Y: np.array, Text: list, Timestamp, figsize=(7, 3), fmt="%d-%b-%Y %I:%M:%S %p"):
    filename = filename if filename.lower().endswith('.pdf') else filename + '.pdf'
    with PdfPages(filename) as pdf:
        for y, text, timestamp in zip(Y, Text, Timestamp):
            fig = plt.figure(figsize=figsize)
            plt.plot(y)
            plt.xticks([], [])
            plt.yticks([], [])
            datetime_s = datetime.datetime.fromtimestamp(timestamp).strftime(fmt)
            plt.xlabel(f'{datetime_s} | {text}', color='red', fontsize='large')
            pdf.savefig(fig)
            plt.close()
