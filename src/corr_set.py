'''
corr_set.py  -->  "correlation set"

this is a class is used to get and store
the correlations of feature values with PHQ-labels
'''

from avf_set import avfSet as avf
import pandas as pd
import os
import numpy as np

class corrSet:
    def __init__(self,avf_set):
        self.avf_set = avf_set

        # create a table of features and correlation coefficients
        self.corr_set = pd.DataFrame(index=["corr_coeff"])
        for i,av in enumerate(self.avf_set.av_features):
            self.corr_set.insert(i,av,0.0)

        # need to load the labels