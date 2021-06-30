'''
load_avec_features.py
Helper functions to get avec feature data from csv (for each patient)
'''

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

class avecFeatures:
    def __init__(self, patient_num, avec_path_prefix):
        
        # data sample index
        self.patient_num = patient_num

        # location of data
        self.avec_path_prefix = avec_path_prefix #"../../avec_data/"

        # create a pandas dataframe from geneva features csv
        self.patient_egemaps = self.get_egemaps()

        # create a pandas dataframe from the MFCCs and deltas
        self.mfccs = self.get_mfccs()

    # extracts the geneva features as a pandas dataframe
    def get_egemaps(self):
        path = os.path.join(self.avec_path_prefix,
                            (str(self.patient_num)+"_P/features/"),
                            (str(self.patient_num)+"_OpenSMILE2.3.0_egemaps.csv"))
        return pd.read_csv(path,sep=";")

    # extract the mfccs as a pandas dataframe
    def get_mfccs(self):
        path = os.path.join(self.avec_path_prefix,
                            (str(self.patient_num)+"_P/features/"),
                            (str(self.patient_num)+"_OpenSMILE2.3.0_mfcc.csv"))
        return pd.read_csv(path,sep=";")

    # get the f1 frequencies as a numpy array
    def get_f1(self):
        return self.patient_egemaps["F1frequency_sma3nz"].values

    # get the f2 frequencies as a numpy array
    def get_f2(self):
        return self.patient_egemaps["F2frequency_sma3nz"].values

    # get MFCC 0 as a numpy array
    def get_mfcc0(self):
        return self.mfccs["pcm_fftMag_mfcc[0]"].values

    # get MFCC 1 as a numpy array
    def get_mfcc1(self):
        return self.mfccs["pcm_fftMag_mfcc[1]"].values

    # get MFCC 2 as a numpy array
    def get_mfcc2(self):
        return self.mfccs["pcm_fftMag_mfcc[2]"].values

    # get MFCC 3 as a numpy array
    def get_mfcc3(self):
        return self.mfccs["pcm_fftMag_mfcc[3]"].values

    # get MFCC 4 as a numpy array
    def get_mfcc4(self):
        return self.mfccs["pcm_fftMag_mfcc[4]"].values

    # get MFCC 5 as a numpy array
    def get_mfcc5(self):
        return self.mfccs["pcm_fftMag_mfcc[5]"].values

    # get MFCC 6 as a numpy array
    def get_mfcc6(self):
        return self.mfccs["pcm_fftMag_mfcc[6]"].values

    # get MFCC 7 as a numpy array
    def get_mfcc7(self):
        return self.mfccs["pcm_fftMag_mfcc[7]"].values

    # get MFCC 8 as a numpy array
    def get_mfcc8(self):
        return self.mfccs["pcm_fftMag_mfcc[8]"].values

    # get MFCC 9 as a numpy array
    def get_mfcc9(self):
        return self.mfccs["pcm_fftMag_mfcc[9]"].values

    # get MFCC 10 as a numpy array
    def get_mfcc10(self):
        return self.mfccs["pcm_fftMag_mfcc[10]"].values

    # get MFCC 11 as a numpy array
    def get_mfcc11(self):
        return self.mfccs["pcm_fftMag_mfcc[11]"].values

    # get MFCC 12 as a numpy array
    def get_mfcc12(self):
        return self.mfccs["pcm_fftMag_mfcc[12]"].values

    # plots the specified data arrays, data is a list of arrays
    def plot_data(self,data):
        for d in data:
            plt.plot(d)
        plt.show()