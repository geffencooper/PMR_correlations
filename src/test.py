'''
corr_set.py  -->  "correlation set"

this is a class is used to get and store
the correlations of feature values with PHQ-labels
'''

from avf_set import avfSet
from corr_set import corrSet
import pandas as pd
import os
import numpy as np


if __name__ == "__main__":
    
    # table = avfSet("../../avec_data/")
    # print(table.avf_set)
    # table.avf_set.to_csv("patient_features.csv")
    features_path = "../../avec_data/patient_features.csv"
    labels_path = "../../avec_data/Detailed_PHQ8_Labels.csv"
    c = corrSet(features_path,labels_path)