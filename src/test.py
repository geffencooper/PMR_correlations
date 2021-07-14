from avf_set import avfSet
from corr_set import corrSet
from transcript_parser import transcriptParser as tp
import pandas as pd
import os
import numpy as np
import librosa
import sounddevice as sd
import time



if __name__ == "__main__":
    
    '''extract features for all patients'''
    # table = avfSet("../../avec_data/")
    # print(table.avf_set)
    # table.avf_set.to_csv("../data/patient_features.csv")

    '''correlations'''
    # features_path = "../data/patient_features.csv"
    # # labels_path = "../data/Detailed_PHQ8_Labels.csv"
    # # c = corrSet(features_path,labels_path)

    '''get the text time splices'''
    # txt_parser = tp("../../avec_data/")
        
    # starts,ends = txt_parser.get_time_splices_2("300",["igh","oi","ai","ie","ia"])

    # test_text = True

    # if test_text:
    #     interview, sr = librosa.load("../../avec_data/300_P/300_AUDIO.wav")

    #     sp = 1/sr
    #     print(sp)
    #     print(len(interview))
        

    #     chunks = []
    #     for i, splice in enumerate(starts):
    #         chunks.append(interview[int(starts[i]/sp):int(ends[i]/sp)]) 
    #     n=0
    #     while True:
    #         n = int(input("enter n"))
    #         sd.play(chunks[n],sr)
    #         print(starts[n])
    #         print(ends[n])
    #         time.sleep(2)
    #         sd.stop()




    '''current test'''
    
    # features from all data
    # table = avfSet("../../avec_data/",None)
    # table.avf_set.to_csv("../data/patient_features.csv")

    # features_path = "../data/patient_features.csv"
    # labels_path = "../data/Detailed_PHQ8_Labels.csv"

    # c = corrSet(features_path,labels_path)
    # phq_scores = ["PHQ_8NoInterest","PHQ_8Depressed","PHQ_8Sleep","PHQ_8Tired","PHQ_8Appetite","PHQ_8Failure","PHQ_8Concentrating","PHQ_8Moving","PHQ_8Total"]
    # for score in phq_scores:
    #     c.calc_corr("../data/correlations"+score+ ".csv",[score])

    
    # features from segments with vowel transitions
    # table = avfSet("../../avec_data/",["igh","oi","ai","ie","ia","ime","ike","ua"])
    # table.avf_set.to_csv("../data/patient_features_filtered.csv")

    features_path = "../data/patient_features_filtered.csv"
    labels_path = "../data/Detailed_PHQ8_Labels.csv"

    c = corrSet(features_path,labels_path)
    phq_scores = ["PHQ_8NoInterest","PHQ_8Depressed","PHQ_8Sleep","PHQ_8Tired","PHQ_8Appetite","PHQ_8Failure","PHQ_8Concentrating","PHQ_8Moving","PHQ_8Total"]
    for score in phq_scores:
        c.calc_corr("../data/correlations_filtered"+score+ ".csv",[score])

    c = corrSet(features_path,labels_path)
    c.plot_values("au_12","PHQ_8Total")
        

