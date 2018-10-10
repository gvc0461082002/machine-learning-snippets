# Define the training data
import numpy as np

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