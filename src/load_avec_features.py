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

    # extracts the geneva features as a pandas dataframe
    def get_egemaps(self):
        path = os.path.join(self.avec_path_prefix,
                            (str(self.patient_num)+"_P/features/"),
                            (str(self.patient_num)+"_OpenSMILE2.3.0_egemaps.csv"))
        return pd.read_csv(path,sep=";")

    # get the f1 frequencies as a numpy array
    def get_f1(self):
        return self.patient_egemaps["F1frequency_sma3nz"].values

    # get the f2 frequencies as a numpy array
    def get_f2(self):
        return self.patient_egemaps["F2frequency_sma3nz"].values

    # plots the specified data arrays, data is a list of arrays
    def plot_data(self,data):
        for d in data:
            plt.plot(d)
        plt.show()