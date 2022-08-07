#install required libraries
import pandas as pd
import numpy as np
#data visualization packages
import matplotlib.pyplot as plt
import random 
#keras packages
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils




(X_train, y_train), (X_test, y_test) = mnist.load_data()
print ("X_train shape", X_train.shape)
print ("y_train shape", y_train.shape)
print ("X_test shape", X_test.shape)
print ("y_test shape", y_test.shape)




plt.rcParams['figure.figsize'] = (9,9)
for i in range (9):
    plt.subplot(3,3,i+1)
    num = random.randint (0, len(X_train))
    plt.imshow(X_train[num], cmap='gray', interpolation = 'none')
    plt.title("Class {}".format(y_train[num]))

plt.tight_layout()





