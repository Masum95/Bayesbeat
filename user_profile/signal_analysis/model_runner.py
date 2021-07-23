import numpy as np
import pandas as pd
import os
import torch
from torch.nn import functional as F
from user_profile.signal_analysis.models.deepbeat_bayesian import Bayesian_Deepbeat
import math
import json
import random

import heartpy as hp
import matplotlib.pyplot as plt
from scipy.signal import resample
import sys
from sklearn.preprocessing import scale
from sklearn.preprocessing import minmax_scale


def run_model_new(model_path, final_tens):
    model = Bayesian_Deepbeat()
    model.load_state_dict(torch.load(model_path)['state_dict'])
    model.eval()
    with torch.no_grad():
        outputs, _ = model(final_tens)
        # outputs = F.log_softmax(outputs, dim=1)
        # outputs = torch.exp(outputs)
    return outputs.numpy()


# reading csv file
# 0-NonAF, 1-AF
def get_prediction(model_path, final_output):
    #    Following program takes csv_directory as input, does necessary operations and then outputs another csv in same directory.
    #    :param csv_filepath // path where all csv files will be stored
    #    :return:

    final_tens = torch.Tensor(final_output).view(-1, 1, 800)

    return np.argmax(run_model_new(model_path, final_tens), axis=1).tolist()
