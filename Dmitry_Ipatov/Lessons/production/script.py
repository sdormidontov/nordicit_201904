import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

import _pickle as cPickle

def main(data):
    with open('iris.pkl', 'rb') as fid:
        dt = cPickle.load(fid)
        
    
    sample = np.array([[
                        data['sepal-length'], 
                        data['sepal-width'], 
                        data['petal-length'], 
                        data['petal-width']
                      ]])
    
    print(dt.predict(sample)[0])
    
    
if __name__ == "__main__":
    main({'sepal-length': 5, 'sepal-width': 3,  'petal-length': 1.6, 'petal-width': 0.5})