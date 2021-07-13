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
                            "mfcc0","mfcc1","mfcc2","mfcc3","mfcc4","mfcc5","mfcc6","mfcc7","mfcc8","mfcc9","mfcc10","mfcc11","mfcc12", \
                            "mfcc0_de","mfcc1_de","mfcc2_de","mfcc3_de","mfcc4_de","mfcc5_de","mfcc6_de","mfcc7_de","mfcc8_de","mfcc9_de","mfcc10_de","mfcc11_de","mfcc12_de", \
                            "F0_var", "F0_std", "Loudness_var", "Loudness_std","jitter","shimmer","hnr", \
                            "au_12","au_14","au_15","vert_head_pitch","vert_eye_gaze"]
        
        # create a table of patients and the corresponding features
        self.avf_set = pd.DataFrame(index=self.patients)
        for i,av in enumerate(self.av_features):
            self.avf_set.insert(i,av,0.0)

        # used to get the start and end splices for the desired portions
        self.txt_parser = tp("../../avec_data/")
        
        # extract the feature values and fill the table
        for patient_i, patient in enumerate(self.patients): # iterate over the rows
            start_times,end_times = self.txt_parser.get_time_splices(patient[:-2],chunk_list)
            #start_samples,end_samples = self.txt_parser.convert_time_to_row(start_times,end_times)
            self.extract_features(patient[:-2],start_times,end_times)
            print("patient:",patient,"num responses:",len(start_times))

    def extract_features(self, patient_num,start_times=None,end_times=None):
        patient = lf(patient_num, self.avec_path_prefix)
        patient_index = str(patient_num)+"_P"

        # get desired audio features
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

        del_mfcc0 = patient.get_mfcc0_delta()
        del_mfcc1 = patient.get_mfcc1_delta()
        del_mfcc2 = patient.get_mfcc2_delta()
        del_mfcc3 = patient.get_mfcc3_delta()
        del_mfcc4 = patient.get_mfcc4_delta()
        del_mfcc5 = patient.get_mfcc5_delta()
        del_mfcc6 = patient.get_mfcc6_delta()
        del_mfcc7 = patient.get_mfcc7_delta()
        del_mfcc8 = patient.get_mfcc8_delta()
        del_mfcc9 = patient.get_mfcc9_delta()
        del_mfcc10 = patient.get_mfcc10_delta()
        del_mfcc11 = patient.get_mfcc11_delta()
        del_mfcc12 = patient.get_mfcc12_delta()

        f0 = patient.get_f0()
        loudness = patient.get_loudness()

        jitter = patient.get_jitter()
        shimmer = patient.get_shimmer()
        hnr = patient.get_hnr()


        # get desired facial features
        au12 = patient.get_au12()
        au14 = patient.get_au14()
        au15 = patient.get_au15()

        head_pitch = patient.get_head_pitch()
        eye_gaze = patient.get_eye_gaze()

        # put into a list
        base_audio_features = [f1,f2,mfcc0,mfcc1,mfcc2,mfcc3,mfcc4,mfcc5,mfcc6,mfcc7,mfcc8,mfcc9,mfcc10,mfcc11,mfcc12,del_mfcc0,del_mfcc1,del_mfcc2,del_mfcc3,del_mfcc4,del_mfcc5,del_mfcc6,del_mfcc7,del_mfcc8,del_mfcc9,del_mfcc10,del_mfcc11,del_mfcc12,f0,loudness,jitter,shimmer,hnr]

        base_visual_features = [au12,au14,au15,head_pitch,eye_gaze]

        start_samples,end_samples = self.txt_parser.convert_time_to_row(100,start_times,end_times)
        if start_samples != None and end_samples != None:
            # audio feature values at specific times
            f1_filtered=f2_filtered=mfcc0_filtered=mfcc1_filtered=mfcc2_filtered=mfcc3_filtered=mfcc4_filtered= \
            mfcc5_filtered=mfcc6_filtered=mfcc7_filtered=mfcc8_filtered=mfcc9_filtered=mfcc10_filtered=mfcc11_filtered=mfcc12_filtered= \
            del_mfcc0_filtered=del_mfcc1_filtered=del_mfcc2_filtered=del_mfcc3_filtered=del_mfcc4_filtered=del_mfcc5_filtered=del_mfcc6_filtered= \
            del_mfcc7_filtered=del_mfcc8_filtered=del_mfcc9_filtered=del_mfcc10_filtered=del_mfcc11_filtered=del_mfcc12_filtered= \
            f0_filtered=loudness_filtered=jitter_filtered=shimmer_filtered=hnr_filtered = np.zeros(1)
            
            # put into a list
            filtered_base_audio_features = [f1_filtered,f2_filtered,mfcc0_filtered,mfcc1_filtered,mfcc2_filtered,mfcc3_filtered,mfcc4_filtered, \
            mfcc5_filtered,mfcc6_filtered,mfcc7_filtered,mfcc8_filtered,mfcc9_filtered,mfcc10_filtered,mfcc11_filtered,mfcc12_filtered, \
            del_mfcc0_filtered,del_mfcc1_filtered,del_mfcc2_filtered,del_mfcc3_filtered,del_mfcc4_filtered,del_mfcc5_filtered,del_mfcc6_filtered, \
            del_mfcc7_filtered,del_mfcc8_filtered,del_mfcc9_filtered,del_mfcc10_filtered,del_mfcc11_filtered,del_mfcc12_filtered,
            f0_filtered,loudness_filtered,jitter_filtered,shimmer_filtered,hnr_filtered]

            # go over all time splices and append to filtered feature lists
            for start,end in zip(start_samples,end_samples):
                for i,filtered_feature in enumerate(filtered_base_audio_features):
                    filtered_base_audio_features[i]=np.append(filtered_base_audio_features[i],base_audio_features[i][start:end])

            f1_filtered = filtered_base_audio_features[0]
            f2_filtered = filtered_base_audio_features[1]   
            self.avf_set.at[patient_index,"f1_mean"] = np.mean(f1_filtered)
            self.avf_set.at[patient_index,"f2_mean"] = np.mean(f2_filtered)

            self.avf_set.at[patient_index,"f1_var"] = np.var(f1_filtered)
            self.avf_set.at[patient_index,"f2_var"] = np.var(f2_filtered)

            self.avf_set.at[patient_index,"f1_std"] = np.std(f1_filtered)
            self.avf_set.at[patient_index,"f2_std"] = np.std(f2_filtered)

            self.avf_set.at[patient_index,"f1_range"] = np.max(f1_filtered) - np.min(f1_filtered)
            self.avf_set.at[patient_index,"f2_range"] = np.max(f2_filtered) - np.min(f2_filtered)

            self.avf_set.at[patient_index,"mfcc0"] = np.mean(filtered_base_audio_features[2])
            self.avf_set.at[patient_index,"mfcc1"] = np.mean(filtered_base_audio_features[3])
            self.avf_set.at[patient_index,"mfcc2"] = np.mean(filtered_base_audio_features[4])
            self.avf_set.at[patient_index,"mfcc3"] = np.mean(filtered_base_audio_features[5])
            self.avf_set.at[patient_index,"mfcc4"] = np.mean(filtered_base_audio_features[6])
            self.avf_set.at[patient_index,"mfcc5"] = np.mean(filtered_base_audio_features[7])
            self.avf_set.at[patient_index,"mfcc6"] = np.mean(filtered_base_audio_features[8])
            self.avf_set.at[patient_index,"mfcc7"] = np.mean(filtered_base_audio_features[9])
            self.avf_set.at[patient_index,"mfcc8"] = np.mean(filtered_base_audio_features[10])
            self.avf_set.at[patient_index,"mfcc9"] = np.mean(filtered_base_audio_features[11])
            self.avf_set.at[patient_index,"mfcc10"] = np.mean(filtered_base_audio_features[12])
            self.avf_set.at[patient_index,"mfcc11"] = np.mean(filtered_base_audio_features[13])
            self.avf_set.at[patient_index,"mfcc12"] = np.mean(filtered_base_audio_features[14])

            self.avf_set.at[patient_index,"mfcc0_de"] = np.mean(filtered_base_audio_features[15])
            self.avf_set.at[patient_index,"mfcc1_de"] = np.mean(filtered_base_audio_features[16])
            self.avf_set.at[patient_index,"mfcc2_de"] = np.mean(filtered_base_audio_features[17])
            self.avf_set.at[patient_index,"mfcc3_de"] = np.mean(filtered_base_audio_features[18])
            self.avf_set.at[patient_index,"mfcc4_de"] = np.mean(filtered_base_audio_features[19])
            self.avf_set.at[patient_index,"mfcc5_de"] = np.mean(filtered_base_audio_features[20])
            self.avf_set.at[patient_index,"mfcc6_de"] = np.mean(filtered_base_audio_features[21])
            self.avf_set.at[patient_index,"mfcc7_de"] = np.mean(filtered_base_audio_features[22])
            self.avf_set.at[patient_index,"mfcc8_de"] = np.mean(filtered_base_audio_features[23])
            self.avf_set.at[patient_index,"mfcc9_de"] = np.mean(filtered_base_audio_features[24])
            self.avf_set.at[patient_index,"mfcc10_de"] = np.mean(filtered_base_audio_features[25])
            self.avf_set.at[patient_index,"mfcc11_de"] = np.mean(filtered_base_audio_features[26])
            self.avf_set.at[patient_index,"mfcc12_de"] = np.mean(filtered_base_audio_features[27])

            self.avf_set.at[patient_index,"F0_var"] = np.var(filtered_base_audio_features[28])
            self.avf_set.at[patient_index,"F0_std"] = np.std(filtered_base_audio_features[28])
            self.avf_set.at[patient_index,"Loudness_var"] = np.var(filtered_base_audio_features[29])
            self.avf_set.at[patient_index,"Loudness_std"] = np.std(filtered_base_audio_features[29])

            self.avf_set.at[patient_index,"jitter"] = np.var(filtered_base_audio_features[30])
            self.avf_set.at[patient_index,"shimmer"] = np.std(filtered_base_audio_features[31])
            self.avf_set.at[patient_index,"hnr"] = np.var(filtered_base_audio_features[32])



            # visual features
            start_samples,end_samples = self.txt_parser.convert_time_to_row(30,start_times,end_times)
            
             # visual feature values at specific times
            au12_filtered=au_14_filtered=au_15_filtered=head_pitch_filtered=eye_gaze_filtered= np.zeros(1)
            
            # put into a list
            filtered_base_visual_features = [au12_filtered,au_14_filtered,au_15_filtered,head_pitch_filtered,eye_gaze_filtered]

            # go over all time splices and append to filtered feature lists
            for start,end in zip(start_samples,end_samples):
                for i,filtered_feature in enumerate(filtered_base_visual_features):
                    filtered_base_visual_features[i]=np.append(filtered_base_visual_features[i],base_visual_features[i][start:end])
  
            self.avf_set.at[patient_index,"au_12"] = np.mean(filtered_base_visual_features[0])
            self.avf_set.at[patient_index,"au_14"] = np.mean(filtered_base_visual_features[1])
            self.avf_set.at[patient_index,"au_15"] = np.mean(filtered_base_visual_features[2])

            self.avf_set.at[patient_index,"vert_head_pitch"] = np.mean(filtered_base_visual_features[3])
            self.avf_set.at[patient_index,"vert_eye_gaze"] = np.mean(filtered_base_visual_features[4])

        else:
            print("ERROR===============")
            exit()

