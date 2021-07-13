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

        # create a pandas dataframe from the facial features
        self.face_features = self.get_face_features()

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

    # extract facial features as a pandas dataframe
    def get_face_features(self):
        path = os.path.join(self.avec_path_prefix,
                            (str(self.patient_num)+"_P/features/"),
                            (str(self.patient_num)+"_OpenFace2.1.0_Pose_gaze_AUs.csv"))
        return pd.read_csv(path,sep=",")

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

    # get delta MFCC 0 as a numpy array
    def get_mfcc0_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[0]"].values

    # get delta MFCC 1 as a numpy array
    def get_mfcc1_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[1]"].values

    # get delta MFCC 2 as a numpy array
    def get_mfcc2_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[2]"].values

    # get delta MFCC 3 as a numpy array
    def get_mfcc3_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[3]"].values

    # get delta MFCC 4 as a numpy array
    def get_mfcc4_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[4]"].values

    # get delta MFCC 5 as a numpy array
    def get_mfcc5_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[5]"].values

    # get delta MFCC 6 as a numpy array
    def get_mfcc6_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[6]"].values

    # get delta MFCC 7 as a numpy array
    def get_mfcc7_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[7]"].values

    # get delta MFCC 8 as a numpy array
    def get_mfcc8_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[8]"].values

    # get delta MFCC 9 as a numpy array
    def get_mfcc9_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[9]"].values

    # get delta MFCC 10 as a numpy array
    def get_mfcc10_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[10]"].values

    # get delta MFCC 11 as a numpy array
    def get_mfcc11_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[11]"].values

    # get delta MFCC 12 as a numpy array
    def get_mfcc12_delta(self):
        return self.mfccs["pcm_fftMag_mfcc_de[12]"].values

    # get F0 value as a numpy array
    def get_f0(self):
        return self.patient_egemaps["F0semitoneFrom27.5Hz_sma3nz"].values

    # get loudness as a numpy array
    def get_loudness(self):
        return self.patient_egemaps["Loudness_sma3"].values

    # get jitter as a numpy array
    def get_jitter(self):
        return self.patient_egemaps["jitterLocal_sma3nz"].values

    # get shimmer as a numpy array
    def get_shimmer(self):
        return self.patient_egemaps["shimmerLocaldB_sma3nz"].values

    # get HNR as a numpy array
    def get_hnr(self):
        return self.patient_egemaps["HNRdBACF_sma3nz"].values

    # get AU12 as a numpy array
    def get_au12(self):
        return self.face_features["AU12_r"].values

    # get AU14 as a numpy array
    def get_au14(self):
        return self.face_features["AU14_r"].values

    # get AU15 as a numpy array
    def get_au15(self):
        return self.face_features["AU15_r"].values

    # get vertical head pose as a numpy array
    def get_head_pitch(self):
        return self.face_features["pose_Rx"].values

    # get vertical eye gaze angle as a numpy array (avg over both eyes)
    def get_eye_gaze(self):
        return (self.face_features["gaze_0_y"].values + self.face_features["gaze_1_y"].values)/2

    # plots the specified data arrays, data is a list of arrays
    def plot_data(self,data):
        for d in data:
            plt.plot(d)
        plt.show()