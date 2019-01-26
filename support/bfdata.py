import pandas as pd

def getcsv_data(testfile='data/test.csv', trainfile='data/train.csv'):

    '''Read test and train CSV files from the given path
    Parameters
    ----------
    testfile : string(optional)
        csv filename with path required
    trainfile: string(optional)
        csv filename with path required
    '''

    
    #Read CSV data files:
    train = pd.read_csv(trainfile)
    test = pd.read_csv(testfile)
    
    # Including new column named source and giving the value as 'train' / 'test' 
    # to identify from where exactly the data was taken
    train['source']='train'
    test['source']='test'
    
    # Combining the 2 dataframes into a single dataframe
    dataset = pd.concat([train, test],ignore_index=True, sort=False)
    print ('Train dataframe :-', train.shape)
    print ('Test dataframe :-', test.shape)
    print ('Combined dataset dataframe :-', dataset.shape)
    return dataset

def getcsv_train(file1='data/BigMartTrain.csv'):
    #Read CSV data files:
    train = pd.read_csv(file1)
    return train

def getcsv_test(file2='data/BigMartTest.csv'):
    #Read CSV data files:
    test = pd.read_csv(file2)
    return test