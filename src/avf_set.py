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
        self.patients = os.listdir("../../avec_data")

        # the features we want from each patient
        self.av_features = ["f1_mean", "f2_mean", "f1_var", "f2_var", "f1_std", "f2_std", "f1_range", "f2_range", \
                            "mfcc0","mfcc1","mfcc2","mfcc3","mfcc4","mfcc5","mfcc6","mfcc7","mfcc8","mfcc9","mfcc10","mfcc11","mfcc12"]
        
        # create a table of patients and the corresponding features
        self.avf_set = pd.DataFrame(index=self.patients)
        for i,av in enumerate(self.av_features):
            self.avf_set.insert(i,av,0.0)

        # extract the feature values and fill the table
        for patient_i, patient in enumerate(self.patients): # iterate over the rows
            self.extract_features(str(self.patients[patient_i])[:-2])
            if patient_i % 25 == 0:
                print(patient_i)

    def extract_features(self, patient_num,start_samples=None,end_samples=None):
        patient = lf(patient_num, self.avec_path_prefix)

        # get desired features
        f1 = patient.get_f1()
        f2 = patient.get_f2()

        patient_index = str(patient_num)+"_P"

        self.avf_set.at[patient_index,"f1_mean"] = np.mean(f1)
        self.avf_set.at[patient_index,"f2_mean"] = np.mean(f2)

        self.avf_set.at[patient_index,"f1_var"] = np.var(f1)
        self.avf_set.at[patient_index,"f2_var"] = np.var(f2)

        self.avf_set.at[patient_index,"f1_std"] = np.std(f1)
        self.avf_set.at[patient_index,"f2_std"] = np.std(f2)

        self.avf_set.at[patient_index,"f1_range"] = np.max(f1) - np.min(f1)
        self.avf_set.at[patient_index,"f2_range"] = np.max(f2) - np.min(f2)

        self.avf_set.at[patient_index,"mfcc0"] = np.mean(patient.get_mfcc0())
        self.avf_set.at[patient_index,"mfcc1"] = np.mean(patient.get_mfcc1())
        self.avf_set.at[patient_index,"mfcc2"] = np.mean(patient.get_mfcc2())
        self.avf_set.at[patient_index,"mfcc3"] = np.mean(patient.get_mfcc3())
        self.avf_set.at[patient_index,"mfcc4"] = np.mean(patient.get_mfcc4())
        self.avf_set.at[patient_index,"mfcc5"] = np.mean(patient.get_mfcc5())
        self.avf_set.at[patient_index,"mfcc6"] = np.mean(patient.get_mfcc6())
        self.avf_set.at[patient_index,"mfcc7"] = np.mean(patient.get_mfcc7())
        self.avf_set.at[patient_index,"mfcc8"] = np.mean(patient.get_mfcc8())
        self.avf_set.at[patient_index,"mfcc9"] = np.mean(patient.get_mfcc9())
        self.avf_set.at[patient_index,"mfcc10"] = np.mean(patient.get_mfcc10())
        self.avf_set.at[patient_index,"mfcc11"] = np.mean(patient.get_mfcc11())
        self.avf_set.at[patient_index,"mfcc12"] = np.mean(patient.get_mfcc12())

