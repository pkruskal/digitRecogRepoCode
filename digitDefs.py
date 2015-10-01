import numpy as np
import matplotlib.pylab as plt

def makeImageArray(train,indx,plots = 0):
    label = train.iloc[indx,0]
    arr = np.array(train.iloc[indx,1:], dtype=np.uint8)
    arr.resize((28, 28))
    if plots:
        plt.figure()
        plt.imshow(arr)
