'''
corr_set.py  -->  "correlation set"

this is a class is used to get and store
the correlations of feature values with PHQ-labels
'''

#from avf_set import avfSet as avf
import pandas as pd
import os
import numpy as np

class corrSet:
    def __init__(self):
        #self.avf_set = avf_set
        l=["f1_mean", "f2_mean", "f1_var", "f2_var", "f1_std", "f2_std", "f1_range", "f2_range"]
        m=["corr_coeff","cc2","cc3"]
        # create a table of features and correlation coefficients
        self.corr_set = pd.DataFrame(index=m)
        for i,av in enumerate(l):
            self.corr_set.insert(i,av,0.0)

        for j,av in enumerate(l):
            for i,row in enumerate(m):
                self.corr_set[av][row] = i+j
        print(self.corr_set)

if __name__ == "__main__":
    c = corrSet()