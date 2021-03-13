# Script for Data Analysis
# the data set of messages is gonna be analysed

import numpy as np
import pandas as pd
#import seaborn as sns
# import matplotlib.pyplot as plt


# print the "n" first messages of the DataSet
def PrintNMessages(messages, n):
    for mess_number, message in enumerate(messages[:n]):
        print(mess_number,message)


# do to the spacing ( there are more than one space between label and message), we can see it is beeing used the tab separator between label and message
# therefore we have a TSV (tab separator value) file --> text format for storing data in a tabular structure. (each value of a record is separated from the next by a tab character).
def CreateDataFrame(file_name):
    return pd.read_csv(file_name, sep='\t', names=['label','message'])

def GetNFirstElementsDataFrame(data_frame, num):
    print(data_frame.head(num))

def DescribeDataFrame(data_frame):
    print(data_frame.describe())

def DescribeByLabel(data_frame, label_denotation):
    print(data_frame.groupby(label_denotation).describe())


#def AnalyzeLengthMessages(data_frame):
    #data_frame['length'] = data_frame['message'].apply(len) # we add a new feature to the data frame, that is the length of the message
#    GetNFirstElementsDataFrame( data_frame, 3)
    #plt.plot(data_frame['length'])
    #data_frame['length'].plot.hist(bins=50)
