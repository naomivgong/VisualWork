import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

score = pd.DataFrame(pd.read_csv("/Users/naomigong/Coding/Visual-Work/VisualWork/VisualWork Dataset  - Sheet1.csv"))
X = score.drop("Score", axis='columns')
y = score["Score"]

# Normalize the data using Min-Max Scaling
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)


# Define a more complex neural network model with regularization
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01), input_shape=(X_train.shape[1],)))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
model.add(tf.keras.layers.Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model on test data
test_loss, test_mae = model.evaluate(X_test, y_test)

# Make predictions on new data (use X_test for simplicity)
predictions = model.predict(X_test)

# Print test loss and predictions
print("Test Loss:", test_loss)
print("Mean Absolute Error on Test Data:", test_mae)
print("\nPredictions on Test Data:\n", predictions)

'''
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_robust = scaler.fit_transform(X)

#split the data
X_train, X_test, y_train, y_test = train_test_split(X_robust, y, test_size = 0.2)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(1))  # Output layer for regression, no activation function

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model on test data (replace X_test and y_test with your actual test data)
test_loss, test_mae = model.evaluate(X_test, y_test)

'''

'''
model = tf.keras.models.Sequential()
#hidden layers
model.add(tf.keras.layers.Dense(units = 5, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(units = 3, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(units = 3, activation = tf.nn.relu))
#outer layer
model.add(tf.keras.layers.Dense(units = 1))

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

model.fit(X_train, y_train, epochs = 3)
'''