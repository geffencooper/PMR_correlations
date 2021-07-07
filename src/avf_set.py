'''
avf_set.py  -->  "audio visual feature set"

this is a class to organize and work with
features accross patients
'''

from load_avec_features import avecFeatures as lf
import pandas as pd
import os
import numpy as np
from transcript_parser import transcriptParser as tp

class avfSet:
    def __init__(self,avec_path_prefix,chunk_list=None):
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

        # used to get the start and end splices for the desired portions
        txt_parser = tp("../../avec_data/")
        
        # extract the feature values and fill the table
        for patient_i, patient in enumerate(self.patients): # iterate over the rows
            start_times,end_times = txt_parser.get_time_splices(patient[:-2],chunk_list)
            start_samples,end_samples = txt_parser.convert_time_to_row(start_times,end_times)
            self.extract_features(patient[:-2],start_samples,end_samples)
            if patient_i % 25 == 0:
                print(patient_i)

    def extract_features(self, patient_num,start_samples=None,end_samples=None):
        patient = lf(patient_num, self.avec_path_prefix)
        patient_index = str(patient_num)+"_P"

        # get desired features
        f1 = patient.get_f1()
        f2 = patient.get_f2()

        mfcc0 = patient.get_mfcc0()
        mfcc1 = patient.get_mfcc1()
        mfcc2 = patient.get_mfcc2()
        mfcc3 = patient.get_mfcc3()
        mfcc4 = patient.get_mfcc4()
        mfcc5 = patient.get_mfcc5()
        mfcc6 = patient.get_mfcc6()
        mfcc7 = patient.get_mfcc7()
        mfcc8 = patient.get_mfcc8()
        mfcc9 = patient.get_mfcc9()
        mfcc10 = patient.get_mfcc10()
        mfcc11 = patient.get_mfcc11()
        mfcc12 = patient.get_mfcc12()

        # put into a list
        base_features = [f1,f2,mfcc0,mfcc1,mfcc2,mfcc3,mfcc4,mfcc5,mfcc6,mfcc7,mfcc8,mfcc9,mfcc10,mfcc11,mfcc12]

        if start_samples != None and end_samples != None:
            # feature values at specific times
            f1_filtered=f2_filtered=mfcc0_filtered=mfcc1_filtered=mfcc2_filtered=mfcc3_filtered=mfcc4_filtered= \
            mfcc5_filtered=mfcc6_filtered=mfcc7_filtered=mfcc8_filtered=mfcc9_filtered=mfcc10_filtered=mfcc11_filtered=mfcc12_filtered = np.zeros(1)
            
            # put into a list
            filtered_base_features = [f1_filtered,f2_filtered,mfcc0_filtered,mfcc1_filtered,mfcc2_filtered,mfcc3_filtered,mfcc4_filtered, \
            mfcc5_filtered,mfcc6_filtered,mfcc7_filtered,mfcc8_filtered,mfcc9_filtered,mfcc10_filtered,mfcc11_filtered,mfcc12_filtered]

            # go over all time splices and append to filtered feature lists
            for start,end in zip(start_samples,end_samples):
                for i,filtered_feature in enumerate(filtered_base_features):
                    filtered_base_features[i]=np.append(filtered_base_features[i],base_features[i][start:end])

            f1_filtered = filtered_base_features[0]
            f2_filtered = filtered_base_features[1]   
            self.avf_set.at[patient_index,"f1_mean"] = np.mean(f1_filtered)#need to change to features[i]
            self.avf_set.at[patient_index,"f2_mean"] = np.mean(f2_filtered)

            self.avf_set.at[patient_index,"f1_var"] = np.var(f1_filtered)
            self.avf_set.at[patient_index,"f2_var"] = np.var(f2_filtered)

            self.avf_set.at[patient_index,"f1_std"] = np.std(f1_filtered)
            self.avf_set.at[patient_index,"f2_std"] = np.std(f2_filtered)

            self.avf_set.at[patient_index,"f1_range"] = np.max(f1_filtered) - np.min(f1_filtered)
            self.avf_set.at[patient_index,"f2_range"] = np.max(f2_filtered) - np.min(f2_filtered)

            self.avf_set.at[patient_index,"mfcc0"] = np.mean(filtered_base_features[2])
            self.avf_set.at[patient_index,"mfcc1"] = np.mean(filtered_base_features[3])
            self.avf_set.at[patient_index,"mfcc2"] = np.mean(filtered_base_features[4])
            self.avf_set.at[patient_index,"mfcc3"] = np.mean(filtered_base_features[5])
            self.avf_set.at[patient_index,"mfcc4"] = np.mean(filtered_base_features[6])
            self.avf_set.at[patient_index,"mfcc5"] = np.mean(filtered_base_features[7])
            self.avf_set.at[patient_index,"mfcc6"] = np.mean(filtered_base_features[8])
            self.avf_set.at[patient_index,"mfcc7"] = np.mean(filtered_base_features[9])
            self.avf_set.at[patient_index,"mfcc8"] = np.mean(filtered_base_features[10])
            self.avf_set.at[patient_index,"mfcc9"] = np.mean(filtered_base_features[11])
            self.avf_set.at[patient_index,"mfcc10"] = np.mean(filtered_base_features[12])
            self.avf_set.at[patient_index,"mfcc11"] = np.mean(filtered_base_features[13])
            self.avf_set.at[patient_index,"mfcc12"] = np.mean(filtered_base_features[14])
            
        else:

            self.avf_set.at[patient_index,"f1_mean"] = np.mean(f1)
            self.avf_set.at[patient_index,"f2_mean"] = np.mean(f2)

            self.avf_set.at[patient_index,"f1_var"] = np.var(f1)
            self.avf_set.at[patient_index,"f2_var"] = np.var(f2)

            self.avf_set.at[patient_index,"f1_std"] = np.std(f1)
            self.avf_set.at[patient_index,"f2_std"] = np.std(f2)

            self.avf_set.at[patient_index,"f1_range"] = np.max(f1) - np.min(f1)
            self.avf_set.at[patient_index,"f2_range"] = np.max(f2) - np.min(f2)

            self.avf_set.at[patient_index,"mfcc0"] = np.mean(mfcc0)
            self.avf_set.at[patient_index,"mfcc1"] = np.mean(mfcc1)
            self.avf_set.at[patient_index,"mfcc2"] = np.mean(mfcc2)
            self.avf_set.at[patient_index,"mfcc3"] = np.mean(mfcc3)
            self.avf_set.at[patient_index,"mfcc4"] = np.mean(mfcc4)
            self.avf_set.at[patient_index,"mfcc5"] = np.mean(mfcc5)
            self.avf_set.at[patient_index,"mfcc6"] = np.mean(mfcc6)
            self.avf_set.at[patient_index,"mfcc7"] = np.mean(mfcc7)
            self.avf_set.at[patient_index,"mfcc8"] = np.mean(mfcc8)
            self.avf_set.at[patient_index,"mfcc9"] = np.mean(mfcc9)
            self.avf_set.at[patient_index,"mfcc10"] = np.mean(mfcc10)
            self.avf_set.at[patient_index,"mfcc11"] = np.mean(mfcc11)
            self.avf_set.at[patient_index,"mfcc12"] = np.mean(mfcc12)

