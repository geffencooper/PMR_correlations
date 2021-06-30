from avf_set import avfSet
from corr_set import corrSet
import pandas as pd
import os
import numpy as np


if __name__ == "__main__":
    
    # table = avfSet("../../avec_data/")
    # print(table.avf_set)
    # table.avf_set.to_csv("../data/patient_features.csv")

    features_path = "../data/patient_features.csv"
    labels_path = "../data/Detailed_PHQ8_Labels.csv"
    c = corrSet(features_path,labels_path)