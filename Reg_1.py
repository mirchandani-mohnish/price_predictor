import pandas as pd
import numpy as np
import matplotlib.pyplot as mp # The error is only temporary -- Program works



init_sampledf = pd.read_csv("./res/initial_sample.csv");

x = init_sampledf.iloc[:,0]
y = init_sampledf.iloc[:,1]

mp.plot(x,y)
mp.show()
