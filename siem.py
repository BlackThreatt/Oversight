import sys

import numpy as np
import pandas as pd
from keras.engine.saving import load_model
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

classes = pd.read_csv("classes.csv", delimiter=',')
samples = pd.read_csv("samples.csv", delimiter=',')

labels = samples['result']

features = samples.iloc[:, :-1]

# save np.load
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

# restore np.load for future normal usage
np.load = np_load_old

model = load_model('NeuralNetwork.h5')

results = model.predict(features)
np.set_printoptions(threshold=sys.maxsize)
print(results.round())

######"""# %split
# x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.33, random_state=15)

############# predict test split
# results = model.predict(x_test)
# results = results.round()
# print(results)
#

############ reverse transform
encoded_results = np.zeros((results.shape[0], 1), int)
for i in range(results.shape[0]):
    encoded_results[i] = np.argmax(results[i])
final_results = labelEncoder.inverse_transform(np.ravel(encoded_results))
print(final_results)

######evaluation

# print(y_test)
# scores = model.evaluate(x_test, y_test, verbose=0)
#
# print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))
