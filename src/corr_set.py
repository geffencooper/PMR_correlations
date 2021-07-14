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
        self.avf_set = pd.read_csv(avf_path,index_col=0)
        self.labels = pd.read_csv(labels_path)

        # create a table of features and correlation coefficients
        self.corr_set = pd.DataFrame(index=["spearman_corr_coeff","spearman_p","spearman_meaningful","pearson_corr_coeff","pearson_p","pearson_meaningful"])
        for i,av in enumerate(self.corr_set):
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
        print(phq_scores)
        for feature in self.avf_set:
            corr, p = stats.spearmanr(self.avf_set[feature].values,phq_values)
            self.corr_set.at["spearman_corr_coeff",feature] = corr
            self.corr_set.at["spearman_p",feature] = p
            if p < 0.05:
                self.corr_set.at["spearman_meaningful",feature] = 1
                print("{:15s} sp_corr: {:5.5f}    p: {:5.5f}".format(feature, corr, p))
            else:
                self.corr_set.at["spearman_meaningful",feature] = 0

            corr, p = stats.pearsonr(self.avf_set[feature].values,phq_values)
            self.corr_set.at["pearson_corr_coeff",feature] = corr
            self.corr_set.at["pearson_p",feature] = p
            if p < 0.05:
                self.corr_set.at["pearson_meaningful",feature] = 1
                print("{:15s} pn_corr: {:5.5f}    p: {:5.5f}".format(feature, corr, p))
            else:
                self.corr_set.at["pearson_meaningful",feature] = 0

        self.corr_set.to_csv(csv_out_path)
        
        
        # scores = self.labels["PHQ_8Total"].values
        # plt.scatter(f1_list,scores)
        # plt.show()

    def plot_values(self,feature,score):
        # first extract data for patients that have labels
        label_ids = []
        data_ids = self.avf_set.index

        for index, row in self.labels.iterrows():
            label_ids.append(str(row[0])+"_P")

        to_remove = np.setdiff1d(data_ids,label_ids)
    
        for id in to_remove:
            self.avf_set = self.avf_set.drop(index=id)

        ft = self.avf_set[feature].values
        sc = self.labels[score].values

        plt.scatter(ft,sc)
        plt.show()
