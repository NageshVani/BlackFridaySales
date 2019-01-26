# Make the model, perform cross validation and export submission file.

from sklearn.model_selection import cross_val_score
from sklearn import metrics
import pandas as pd
import numpy as np

def modelfit(algorthm, dftrain, dftest, predictors, target, IDcol, filename=None):

    #Fit the algorthmorithm on the data
    algorthm.fit(dftrain[predictors], dftrain[target]) # similar to the base dataframe created above with the predictor & target columns
        
    #Predict training set:
    dftrain_predictions = algorthm.predict(dftrain[predictors]) # Predicting using the predictors

    #Perform cross-validation:
    cv_score = cross_val_score(algorthm, dftrain[predictors], dftrain[target], cv=20, n_jobs=-1, scoring='neg_mean_squared_error')
    cv_score = np.sqrt(np.abs(cv_score))
    
    #Print model report:
    print ("\n------Model Report----\n")
    print ("RMSE : " , np.sqrt(metrics.mean_squared_error(dftrain[target].values, dftrain_predictions)))
    print ("CV Score Mean : %.4g" %(np.mean(cv_score)))
    print ("CV Score Std : %.4g" %(np.std(cv_score)))
    print ("CV Score Min : %.4g" %(np.min(cv_score)))
    print ("CV Score Max : %.4g" %(np.max(cv_score)))
    
    #Predict on testing data:
    dftest[target] = algorthm.predict(dftest[predictors])
    
    if filename!= None :
        #Export submission file:
        IDcol.append(target)
        submission = pd.DataFrame({ x: dftest[x] for x in IDcol})
        submission.to_csv(filename, index=False)