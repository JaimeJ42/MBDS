#!/usr/bin/python
# -*- coding:utf-8 -*-

#Q3

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
np.set_printoptions(threshold=200000)
model = Sequential()

train_data = np.loadtxt('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 3/train_data.txt', skiprows=1)
train_truth = np.loadtxt('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 3/train_truth.txt', skiprows=1)
test_data = np.loadtxt('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 3/test_data.txt', skiprows=1)

#prevent over fitting, 20% of the neurons were removed randomly
model.add(Dropout(0.2))
#build the input layer and the first hidden layer
#The weight and variance are initialized by using the random number of normal distribution
model.add(Dense(units=4, input_dim=3, kernel_initializer='normal', activation='relu'))
#build the second hidden layer
model.add(Dense(units=4, kernel_initializer='normal', activation='relu'))
#build the output layer
model.add(Dense(units=1, kernel_initializer='normal', activation='sigmoid'))

#define training method
model.compile(loss='mse', optimizer='adam')
#training
model.fit(train_data, train_truth, epochs=100)
#save the model
model.save('Q3_model.h5')

#predict
prediction = model.predict(test_data)
print(prediction)

out_file = open('/Users/jaime/Desktop/blah/AY20_MBDS_questions/Question 3/test_predicted.txt', 'w')
out_file.write('y' + '\n')
for m in range(len(prediction)):
    out_file.write(str(prediction[m][0]))
    out_file.write('\n')
#out_file.write(str(prediction))
out_file.close()
