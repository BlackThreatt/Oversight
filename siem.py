import numpy as np
import pandas as pd
import tensorflow
from keras.engine.saving import load_model
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = pd.read_csv("samples.csv", delimiter=',')

labels = data['result']

features = data.iloc[:, :-1]
# encode the protocol type
protocolTypeEncoder = LabelEncoder()
protocolTypeEncoder.fit(features['protocol_type'])
features['protocol_type'] = protocolTypeEncoder.transform(features['protocol_type'])

# service encoder
serviceEncoder = LabelEncoder()
serviceEncoder.fit(features['service'])
features['service'] = serviceEncoder.transform(features['service'])

# flag encoder
flagEncoder = LabelEncoder()
flagEncoder.fit(features['flag'])
features['flag'] = flagEncoder.transform(features['flag'])

# label encoder
labelEncoder = LabelEncoder()
labelEncoder.fit(labels)
encoded_Y = labelEncoder.transform(labels)
targets = np_utils.to_categorical(encoded_Y)

model = Sequential()
model.add(Dense(45, activation='relu', input_dim=features.shape[1]))
model.add(Dense(45, activation='relu'))
# softmax => sum =1
model.add(Dense(4, activation='softmax'))
# adam optimizer => do not use learning rate
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(features, targets, epochs=20)

x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.33, random_state=42)

# test = pd.read_csv("test.csv", delimiter=',')
# print(model.predict(test))
results = model.predict(x_test)
results = results.round()
for i in range(results.shape[0]):
    print(labelEncoder.inverse_transform(results[i]))
print(results.round()[0])
#print(np.argmax(results.round()))
#print()
print(labelEncoder.inverse_transform(encoded_Y))
scores = model.evaluate(x_test, y_test, verbose=0)

print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))

# save neural networks state
# model.save('classification_model.h5')
# pretrained_model = load_model('classification_model.h5')
