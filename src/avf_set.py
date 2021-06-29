'''
avf_set.py  -->  "audio visual feature set"

this is a class to organize and work with
features accross patients
'''

from load_avec_features import avecFeatures as lf
import pandas as pd
import os
import numpy as np

class avfSet:
    def __init__(self,avec_path_prefix):
        # path to the directory with patient data
        self.avec_path_prefix = avec_path_prefix
        self.patients = os.listdir()

        # the features we want from each patient
        self.av_features = ["f1_mean", "f2_mean", "f1_var", "f2_var", "f1_std", "f2_std", "f1_range", "f2_range"]
        
        # create a table of patients and the corresponding features
        self.avf_set = pd.DataFrame(index=self.patients)
        for i,av in enumerate(self.av_features):
            self.avf_set.insert(i,av,0.0)

        # extract the feature values and fill the table
        for patient_i, patient in enumerate(self.patients): # iterate over the rows
            self.extract_features(patient_i)

    def extract_features(self, patient_num):
        patient = lf(patient_num, self.avec_path_prefix)

        # get desired features
        f1 = patient.get_f1()
        f2 = patient.get_f2()

        self.avf_set.at[patient_num,"f1_mean"] = np.mean(f1)
        self.avf_set.at[patient_num,"f2_mean"] = np.mean(f2)

        self.avf_set.at[patient_num,"f1_var"] = np.var(f1)
        self.avf_set.at[patient_num,"f2_var"] = np.var(f2)

        self.avf_set.at[patient_num,"f1_std"] = np.std(f1)
        self.avf_set.at[patient_num,"f2_std"] = np.std(f2)

        self.avf_set.at[patient_num,"f1_range"] = np.max(f1) - np.min(f1)
        self.avf_set.at[patient_num,"f2_range"] = np.max(f2) - np.min(f2)

