'''
transcript_parser.py

this is a class to help extract the regions
of speech where their may be useful features
'''

import pandas as pd
import os
import numpy as np

class transcriptParser:
    def __init__(self,patient_num,avec_path_prefix):
        self.avec_path_prefix = avec_path_prefix
        self.patient_num = patient_num

        path = os.path.join(self.avec_path_prefix,
                            (str(self.patient_num)+"_P/"),
                            (str(self.patient_num)+"_Transcript.csv"))

        self.transcript = pd.read_csv(path)

        # get the responses as a list and the time stamps as lists
        self.responses = self.transcript['Text'].to_list()
        self.start_times = self.transcript["Start_Time"]
        self.stop_times = self.transcript["End_Time"]

    # gets the approximate start and end times of every iteration
    # of the desired text chunks (ex: /ai/)
    def get_time_splices(self,text_chunks):
        chunk_start_times = []
        chunk_end_times = []

        # list of locations (response index, character index, chunk length)
        chunk_locations = []

        # search for each chunk in each response
        for chunk in text_chunks:
            for resp_i, resp in enumerate(self.responses):
                chunk_i = resp.find(chunk)
                if chunk_i != -1:
                    # the sample period for a response is the total time of the response divided by the number of letters --> (seconds per letter)
                    sample_period = (self.stop_times[resp_i]-self.start_times[resp_i])/(len(resp)+0) # may need to tune how we calculate this sample period
                    
                    # we want to get audio slightly before and after chunk since we have some error in the sample period
                    padding = 2*sample_period

                    # start time is the start of the response in seconds plus the chunk starting location times the sample period
                    start = self.start_times[resp_i] + chunk_i*sample_period - padding

                    # end time is the start time plus the length of the chunk times the sample period
                    end = start + len(chunk)*sample_period + padding

                    # make sure we are in the bounds of the response (padding may take out of bounds)
                    if start < self.start_times[resp_i]:
                        start = self.start_times[resp_i]

                    if end > self.stop_times[resp_i]:
                        end = self.stop_times[resp_i]

                    chunk_start_times.append(start)
                    chunk_end_times.append(end)

        return(chunk_start_times, chunk_end_times)
            
