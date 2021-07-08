'''
transcript_parser.py

this is a class to help extract the regions
of speech where their may be useful features
'''

import pandas as pd
import os
import numpy as np
from load_avec_features import avecFeatures as lf

class transcriptParser:
    def __init__(self,avec_path_prefix):
        self.avec_path_prefix = avec_path_prefix

    # gets the approximate start and end times of every iteration
    # of the desired text chunks (ex: /ai/), if no chunks passed in then return
    # the splices of the responses
    def get_time_splices(self,patient_num,text_chunks):
        # get the transcript
        path = os.path.join(self.avec_path_prefix,
                            (str(patient_num)+"_P/"),
                            (str(patient_num)+"_Transcript.csv"))

        self.transcript = pd.read_csv(path)

        # get the responses as a list and the time stamps as lists
        self.responses = self.transcript['Text'].to_list()
        self.start_times = self.transcript["Start_Time"]
        self.stop_times = self.transcript["End_Time"]

        if text_chunks == None:
            return (self.start_times,self.stop_times)

        
        chunk_start_times = []
        chunk_end_times = []

        # search for each chunk in each response
        for chunk in text_chunks:
            for resp_i, resp in enumerate(self.responses):
                chunk_i=0
                while chunk_i < len(resp):
                    chunk_i = resp.find(chunk,chunk_i)
                    if chunk_i == -1:
                        break

                    # the sample period for a response is the total time of the response divided by the number of letters --> (seconds per letter)
                    sample_period = (self.stop_times[resp_i]-self.start_times[resp_i])/(len(resp)+0) # may need to tune how we calculate this sample period
                    
                    # we want to get audio slightly before and after chunk since we have some error in the sample period
                    padding = 2*sample_period

                    # start time is the start of the response in seconds plus the chunk starting location times the sample period
                    start = self.start_times[resp_i] + chunk_i*sample_period

                    # end time is the start time plus the length of the chunk times the sample period
                    end = start + len(chunk)*sample_period + 8*padding

                    # make sure we are in the bounds of the response (padding may take out of bounds)
                    if start < self.start_times[resp_i]:
                        start = self.start_times[resp_i]

                    if end > self.stop_times[resp_i]:
                        end = self.stop_times[resp_i]

                    chunk_start_times.append(start)
                    chunk_end_times.append(end)

                    chunk_i += len(chunk)

        return(chunk_start_times, chunk_end_times)

    # DO NOT USE, VERY SLOW AND INEFFICIENT
    # modifies the mfcc and egde feature csvs so only have 'interesting sections'
    def generate_filtered_features(self,text_chunks):
        # get all the patients
        patients = os.listdir("../../avec_data")

        # get the features for each patient
        for patient in patients:
            patient_data = lf(patient[:-2], self.avec_path_prefix)
            chunk_start_times, chunk_end_times = self.get_time_splices(patient[:-2],text_chunks)
            print(chunk_start_times)
            print(chunk_end_times)

            # get as panda data frames
            egemaps = patient_data.get_egemaps()
            mfccs = patient_data.get_mfccs()

            chunk_idx = 0
            start = True

            # iterate over all the rows
            for index, row in egemaps.iterrows():
                if index % 1000 == 0:
                    print(index)
                # searching for the start time
                if start:
                    #print(chunk_idx,"-->",row)
                    # while the current time is less than the start time, remove the row
                    if chunk_start_times[chunk_idx] < row["frameTime"]:
                        egemaps.drop(index,inplace=True)
                        mfccs.drop(index,inplace=True)
                    # if the start time is greater than or equal to the current time then transition to end time
                    else:
                        start = False
                # searching for the end time
                else:
                    # while the end time is greater than the current time, continue
                    if chunk_end_times[chunk_idx] > row["frameTime"]:
                        continue
                    # if the end time is less than or equal to the current time, remove the row
                    else:
                        egemaps.drop(index,inplace=True)
                        mfccs.drop(index,inplace=True)

                        # now move on to the next chunk and look for its start time
                        start = True
                        chunk_idx += 1
                        if chunk_idx >= len(chunk_start_times):
                            chunk_idx -=1

            path = os.path.join(self.avec_path_prefix,
                                (patient[:-2]+"_P/features/"),
                                (patient[:-2]+"_OpenSMILE2.3.0_egemaps_filtered.csv"))
            egemaps.to_csv(path)
                
            path = os.path.join(self.avec_path_prefix,
                                (patient[:-2]+"_P/features/"),
                                (patient[:-2]+"_OpenSMILE2.3.0_mfcc_filtered.csv"))
            mfccs.to_csv(path)
            exit()

    def convert_time_to_row(self,start_times,end_times):
        start_samples = []
        end_samples = []
        sample_time = 0.01
        sample_rate = 100

        # for st,et in zip(start_times,end_times):
        #     num_samples = (et-st)/sample_time
        #     start_samples.append(st/sample_time)
        #     end_samples.append(st/sample_time + num_samples)

        start_samples = [int(x*100) for x in start_times]
        end_samples = [int(x*100) for x in end_times]

        return (start_samples, end_samples)


           

            
