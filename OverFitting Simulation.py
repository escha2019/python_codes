#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class overfitting:
    
    def __init__(self):
        pass
    
    def TrueTargetFunct(self):
        
        pass
    
    def AddNoiseTargetFunct(self):
        
        pass
    def plot(self, trueTarget, proposedTarget):
        pass
    
    def TrainTestSplit(self, X, y, degree, test_size = 0.20):
        """fit the data from exercise 4.2 using linear regression
        """
        poly = PolynomialFeatures(degree)

        data = poly.fit_transform(X)
        
        data = pd.DataFrame(data, columns = poly.get_feature_names())
        
        temp = poly.get_feature_names()
        
        # Remove Cross interactions
        [temp.remove(i) for i in poly.get_feature_names() if len(i.split())==2]
        
        data = data[temp]
        
        X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=test_size, random_state=42)
        
        return X_train, X_test, y_train, y_test
    
    
    def removeDataPoints(self, data, size):
        """data -- a list of tuples
           E.g. [(x,y), (x,y), ...]
        """
        return data.remove(np.random.Generator.choice(len(data)-1, replace=False, size = size))
    
    def exerciseFourTwo(self, order, sigma, sampleSize):
        """Generate target function data with random noise using legendre polynomial
           PARAMS:
               order - order of polynomial
               sigma - noise sigma for yn data
               sampleSize - # of data points to generate
        """
        # generate polynomical coefficient
        c = np.random.normal(0, 1, order).reshape(-1, 1)
        c = normalize(c, axis=0).flatten()
        
        # generate uniform input/feature vector
        x = np.random.uniform(-1, 1, sampleSize)
        
        # generate Yi's using legendre polynomial
        y = np.polynomial.legendre.legval(x, c = c)
        
        # add noise to label/target
        y = y + sigma*np.random.normal(0, 1, len(y))
        
        return x.reshape(-1, 1), y.reshape(-1, 1)
    
    def fitExercisefourTwo(self, X, y):
        """fit the data from exercise 4.2 using linear regression
        """
        # run Regression
        reg = LinearRegression().fit(X, y)
        
        return reg
    
    
    def predict(self, model, X, y):
        
        error = np.mean(np.power(model.predict(X) - y, 2))
        
        return error
        
        
    
    def legendrePoly2(self, order, domain):
        
        terms = [1, 1 + domain]
        
        for i in range(2, order+1):
            
            terms.append(((2*i - 1)/i)*domain*terms[i-1] - ((i - 1)/i)*terms[i-2])
            
        return sum(terms), terms
        


# In[2]:


Qf    = range(1, 51)
N     = range(20, 125, 5)
sigma = np.arange(0, 2.05, 0.05)


# In[3]:


v       = overfitting()
error   = []

for leg in Qf:
    for n in N:
        for sig in sigma:
            # generate data
            X, y = v.exerciseFourTwo(order=leg, sigma=sig, sampleSize=n)

            # train test split
            X_train2, X_test2, y_train2, y_test2     = v.TrainTestSplit(X, y, 2)
            X_train10, X_test10, y_train10, y_test10 = v.TrainTestSplit(X, y, 10)
            
            # run two models
            model2,  model10 = v.fitExercisefourTwo(X_train2, y_train2), 
                                      v.fitExercisefourTwo(X_train10, y_train10)
            # get in-sample error
            errorTrainDeg2, errorTrainDeg10 = v.predict(model2, X_train2, y_train2), 
                                      v.predict(model10, X_train10, y_train10)
            # get out-sample error
            errorTestDeg2, errorTestDeg10 = v.predict(model2, X_test2, y_test2), 
                                      v.predict(model10, X_test10, y_test10)
            # errors dictionary
            error.append([errorTrainDeg2, errorTrainDeg10, errorTestDeg2, 
                          errorTestDeg10, leg, n, sig])
            
pd.DataFrame(error, columns=['g2Train','g10Train', 'g2Test','g10Test', 
             'degLegredre', 'size', 'sigma']).to_excel("overfittingSimulation.xlsx", index=False)

