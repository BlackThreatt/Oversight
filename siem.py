from datetime import datetime
from os import listdir
from os.path import isfile, join

import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch
from keras.engine.saving import load_model
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

mypath = 'users/'
# get all users logs
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

lastIndex = 0

classes = pd.read_csv("classes.csv", delimiter=',')
for file in files:
    initialRows = pd.read_csv(mypath + file, delimiter=',').iloc[:, :]
    samples = pd.read_csv(mypath + file, delimiter=',')

    print(files)

    # intialize the labels
    labels = classes['result']

    # initialize the features
    features = samples.iloc[:, :]

    ##### encode the features (preprocessing)
    #### save np.load
    np_load_old = np.load

    # modify the default parameters of np.load
    np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)

    # encode the protocol type
    protocolTypeEncoder = LabelEncoder()
    protocolTypeEncoder.classes_ = np.load('encodedProtocol.npy')
    features['protocol_type'] = protocolTypeEncoder.transform(features['protocol_type'])

    # service encoder
    serviceEncoder = LabelEncoder()
    serviceEncoder.classes_ = np.load('encodedService.npy')
    features['service'] = serviceEncoder.transform(features['service'])

    # flag encoder
    flagEncoder = LabelEncoder()
    flagEncoder.classes_ = np.load('encodedFlag.npy')
    features['flag'] = flagEncoder.transform(features['flag'])

    # label encoder
    labelEncoder = LabelEncoder()
    labelEncoder.classes_ = np.load('encodedLabel.npy')
    encoded_Y = labelEncoder.transform(labels)
    print(encoded_Y.shape)
    targets = np_utils.to_categorical(encoded_Y)

    ##### restore np.load for future normal usage
    np.load = np_load_old

    ###### load model
    model = load_model('NeuralNetwork.h5')

    ###### predict
    results = model.predict(features)

    ##initialize the econded results
    encoded_results = np.zeros((results.shape[0], 1), int)

    es = Elasticsearch(['http://elastic:changeme@localhost:9200'])
    delemiterIndex = file.index('.')
    userid = file[:delemiterIndex]
    print('---------------------------------', userid)
    for i in range(results.shape[0]):
        encoded_results[i] = np.argmax(results[i])
        ##Initialize the body
        doc = {
            'userID': userid,
            'type': labelEncoder.inverse_transform(np.ravel(encoded_results[i]))[0],
            'body': pd.DataFrame(initialRows.loc[i, :]).to_string(),
            'timestamp': datetime.now(),
        }
        print(labelEncoder.inverse_transform(np.ravel(encoded_results[i])))
        print(initialRows.loc[i, :])
        print("---------------------")
        id_lig = i + lastIndex
        # posting the new threat to index it at elasticsearch
        res = es.index(index="threat", doc_type='tweet', id=id_lig, body=doc)

        print(res['result'])

        # getting the new values of the threat index
        res = es.get(index="threat", doc_type='tweet', id=id_lig)
        print(res['_source'])
    lastIndex += results.shape[0] + 1
print(lastIndex)
