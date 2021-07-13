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
    # txt_parser = tp(300,"../../avec_data/")
    # starts,ends = txt_parser.get_time_splices(["ou"])

    # test_text = False

    # if test_text:
    #     interview, sr = librosa.load("../../avec_data/300_P/300_AUDIO.wav")

    #     sp = 1/sr
    #     print(sp)
    #     print(len(interview))
        

    #     chunks = []
    #     for i, splice in enumerate(starts):
    #         chunks.append(interview[int(starts[i]/sp):int(ends[i]/sp)]) 

    #     sd.play(chunks[1],sr)
    #     print(starts[1])
    #     print(ends[1])
    #     time.sleep(3)
    #     sd.stop()

    '''current test'''
    # table = avfSet("../../avec_data/",["ou","igh","oi","ai"])
    # table.avf_set.to_csv("../data/patient_features_filtered.csv")
    # table = avfSet("../../avec_data/",None)
    # table.avf_set.to_csv("../data/patient_features.csv")

    # features_path = "../data/patient_features.csv"
    # labels_path = "../data/Detailed_PHQ8_Labels.csv"
    # c = corrSet(features_path,labels_path)
    # c.calc_corr("../data/correlations.csv",["PHQ_8Moving"])

    txt_parser = tp("../../avec_data/")
    start_times,end_times = txt_parser.get_time_splices_2("300",None)
    print(start_times)
    print(end_times)

    
        

