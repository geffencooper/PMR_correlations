from avf_set import avfSet
from corr_set import corrSet
from transcript_parser import transcriptParser as tp
import pandas as pd
import os
import numpy as np


if __name__ == "__main__":
    
    # table = avfSet("../../avec_data/")
    # print(table.avf_set)
    # table.avf_set.to_csv("../data/patient_features.csv")

    # features_path = "../data/patient_features.csv"
    # # labels_path = "../data/Detailed_PHQ8_Labels.csv"
    # # c = corrSet(features_path,labels_path)

    txt_parser = tp(300,"../../avec_data/")
    splices = txt_parser.get_time_splices(["ou"])

    print(len(splices[0]))
    print(splices[0])
    print(splices[1])

