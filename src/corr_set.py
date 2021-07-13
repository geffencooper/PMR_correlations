'''
corr_set.py  -->  "correlation set"

this is a class is used to get and store
the correlations of feature values with PHQ-labels
'''

from avf_set import avfSet as avf
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class corrSet:
    def __init__(self,avf_path,labels_path):
        # load the features and the labels
        self.avf_set = pd.read_csv(avf_path)
        self.labels = pd.read_csv(labels_path)

        # create a table of features and correlation coefficients
        self.corr_set = pd.DataFrame(index=["corr_coeff","p"])
        for i,av in enumerate(self.avf_set):
            self.corr_set.insert(i,av,0.0)

    def calc_corr(self,csv_out_path,phq_scores):
        # first extract data for patients that have labels
        label_ids = []
        data_ids = self.avf_set.index

        for index, row in self.labels.iterrows():
            label_ids.append(str(row[0])+"_P")

        to_remove = np.setdiff1d(data_ids,label_ids)
        
        for id in to_remove:
            self.avf_set = self.avf_set.drop(index=id)

        # initialize an empty scores array
        phq_values = np.zeros(len(self.labels[phq_scores[0]]))

        # sum accross the desired scores
        for score in phq_scores:
            phq_values += self.labels[score].values

        # now find all the correlation coefficients
        for feature in self.avf_set:
            corr, p = stats.spearmanr(self.avf_set[feature].values,phq_values)
            self.corr_set.at["corr_coeff",feature] = corr
            self.corr_set.at["p",feature] = p
            print("feature:", feature, "---> corr:", corr, "p: ", p)
        self.corr_set.to_csv(csv_out_path)
        
        
        # scores = self.labels["PHQ_8Total"].values
        # plt.scatter(f1_list,scores)
        # plt.show()
