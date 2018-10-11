# Define the training data
import numpy as np
import matplotlib.pyplot as plt
X_train = np.random.random((5000, 32))
y_train = np.random.random((5000, 5))

# Define the neural network model
from keras import models
from keras import layers

INPUT_DIM = X_train.shape[1]
print(INPUT_DIM)
model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_dim=INPUT_DIM))
model.add(layers.Dense(5, activation='softmax'))

# Configure the learning process
from keras import optimizers
from keras import metrics

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train,
          batch_size=128,
          epochs=10)
y_predict = model.predict(X_train[1:20])

plt.plot(y_train[1:20]-y_predict)
plt.ylabel('prediction')
plt.show()