import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

# load data from dataset
data = pd.read_csv("dataset.csv", delimiter=',')

# get labels
labels = data['result']
# get features
features = data.iloc[:, :-1]

# encode the protocol type
protocolTypeEncoder = LabelEncoder()
protocolTypeEncoder.fit(features['protocol_type'])
np.save('encodedProtocol.nps', protocolTypeEncoder.classes_)
features['protocol_type'] = protocolTypeEncoder.transform(features['protocol_type'])

# service encoder
serviceEncoder = LabelEncoder()
serviceEncoder.fit(features['service'])
np.save('encodedService.nps', serviceEncoder.classes_)
features['service'] = serviceEncoder.transform(features['service'])

# flag encoder
flagEncoder = LabelEncoder()
flagEncoder.fit(features['flag'])
np.save('encodedFlag.nps', flagEncoder.classes_)
features['flag'] = flagEncoder.transform(features['flag'])

# label encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(labels)
np.save('encodedLabel.nps', labelEncoder.classes_)
encoded_Y = labelEncoder.transform(labels)
print(encoded_Y.shape)
targets = np_utils.to_categorical(encoded_Y)

# create model
model = Sequential()
model.add(Dense(45, activation='relu', input_dim=features.shape[1]))
model.add(Dense(45, activation='relu'))
## softmax => sum =1
model.add(Dense(23, activation='softmax'))
## adam optimizer => do not use learning rate
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
## train 20 times
model.fit(features, targets, epochs=20)

model.save('NeuralNetworkTest.h5')
