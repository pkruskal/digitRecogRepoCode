import digitDefs
import pandas as pd
import matplotlib.pylab as plt

# load data
train = pd.read_csv('../data/train.csv')

digitDefs.makeImageArray(train,2,plots = 1)
