# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:12:29 2019

Basic scipt to import the TRAIN data set in pandas.
Identify events and split the data set. 

@author: karaouli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Stored data and redorded data have differetn frequncy sample. REMEMBER
dt=0.0375  #sampling rate (to be used later for FFT)
f=4e6 # Reforded frequency
no_of_points=150000


# Read traing data set. It takes time and it's too big in one go. Use chunksize
df=pd.DataFrame()
for chunk in pd.read_csv('train.csv', dtype={'acoustic_data':np.int32,'time_to_failure':np.float64}, chunksize=10000000):
    df = pd.concat([df, chunk], ignore_index=True)

##df.to_hdf('train.hdf','train',mode='w')
#df=pd.read_hdf('train.hdf','train')



# identify events in the data set and split the data. Every next event,
# resets the time counter. We shoud see the events indiviudal and see what happens
# on the data before each "earthquake". Anyhow....
dt_del=df.iloc[1:,1].values-df.iloc[:-1,1].values
ix=np.where(dt_del>=0)[0]+1  # number of events
#df.iloc[ix[0],1].values


    