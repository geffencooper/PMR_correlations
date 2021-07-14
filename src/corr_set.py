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

        labels_sp = []
        labels_pn = []
        sp_c = []
        sp_p = []
        pn_c =  []
        pn_p = []

        # now find all the correlation coefficients
        print(phq_scores)
        for feature in self.avf_set:
            corr, p = stats.spearmanr(self.avf_set[feature].values,phq_values)
            self.corr_set.at["spearman_corr_coeff",feature] = corr
            self.corr_set.at["spearman_p",feature] = p
            if p < 0.05:
                self.corr_set.at["spearman_meaningful",feature] = 1
                print("{:15s} sp_corr: {:5.5f}    p: {:5.5f}".format(feature, corr, p))
                labels_sp.append(feature)
                sp_p.append(round(p,3))
                sp_c.append(round(corr,3))
            else:
                self.corr_set.at["spearman_meaningful",feature] = 0

            corr, p = stats.pearsonr(self.avf_set[feature].values,phq_values)
            self.corr_set.at["pearson_corr_coeff",feature] = corr
            self.corr_set.at["pearson_p",feature] = p
            if p < 0.05:
                self.corr_set.at["pearson_meaningful",feature] = 1
                print("{:15s} pn_corr: {:5.5f}    p: {:5.5f}".format(feature, corr, p))
                labels_pn.append(feature)
                pn_p.append(round(p,3))
                pn_c.append(round(corr,3))
            else:
                self.corr_set.at["pearson_meaningful",feature] = 0

        
        x_sp = np.arange(len(labels_sp))
        x_pn = np.arange(len(labels_pn))
        width = 0.35

        fig1,ax1 = plt.subplots()
        fig2,ax2 = plt.subplots()
        
        sc=ax1.bar(x_sp+width/2,sp_c,width,label='Spearman Correlation')
        sp=ax1.bar(x_sp-width/2,sp_p,width,label='P-value')
        pc=ax2.bar(x_pn+width/2,pn_c,width,label='Pearson Correlation')
        pp=ax2.bar(x_pn-width/2,pn_p,width,label='P-value')

        ax1.set_ylabel('Correlation and P values')
        ax1.set_title('Feature Correlation with '+phq_scores[0]+'subscore')
        ax1.set_xticks(x_sp)
        ax1.set_xticklabels(labels_sp)
        ax1.legend()

        ax1.bar_label(sc,padding=3)
        ax1.bar_label(sp,padding=3)

        ax2.set_ylabel('Correlation and P values')
        ax2.set_title('Feature Correlation with '+phq_scores[0]+'subscore')
        ax2.set_xticks(x_pn)
        ax2.set_xticklabels(labels_pn)
        ax2.legend()

        ax2.bar_label(pc,padding=3)
        ax2.bar_label(pp,padding=3)

        dest_path_sp=""
        dest_path_pn=""
        if "filtered" in csv_out_path:
            dest_path_sp = "../data/plots/correlations_filtered_spearman_"+phq_scores[0]+".png"
            dest_path_pn = "../data/plots/correlations_filtered_pearson_"+phq_scores[0]+".png"
        else:
            dest_path_sp = "../data/plots/correlations_spearman_"+phq_scores[0]+".png"
            dest_path_pn = "../data/plots/correlations_pearson_"+phq_scores[0]+".png"

        
        

        fig1.tight_layout()
        fig1.savefig(dest_path_sp)
        fig2.tight_layout()
        fig2.savefig(dest_path_pn)
        plt.show()
        
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
