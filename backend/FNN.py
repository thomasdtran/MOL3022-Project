"""
Feedforward Neural Network
"""
import os
from dotenv import load_dotenv

from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

import numpy as np

from dict import secondary_protein_struct

load_dotenv()

# callback function to stop training when the desired accuracy is >= ACCURACY_THRESHOLD
class myCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        accuracy_threshold = float(os.getenv('ACCURACY_THRESHOLD'))
        if (logs.get('accuracy') > accuracy_threshold):
            print("\nReached {:.2f} accuracy, stops training!!".format(accuracy_threshold))
            self.model.stop_training = True

class FNN:
    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(Flatten(input_shape=input_shape))
        self.model.add(Dense(3, activation='relu'))
        self.model.add(Dense(3, activation='softmax'))
        
        self.lr_schedule = keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=1e-2,
            decay_steps=10000,
            decay_rate=0.9)
        
        self.opt = Adam(learning_rate=self.lr_schedule)
        self.model.compile(
            optimizer=self.opt, loss='categorical_crossentropy', metrics=['accuracy'])
        
        self.callbacks = myCallback()

    def fit(self, X_train, y_train, epochs=200, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs,
                       batch_size=batch_size, callbacks=[self.callbacks])

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test,  y_test)
    
    def save_model(self):
        self.model.save("./saved_model/my_model.h5")
    
    def load_model(self):
        self.model = keras.models.load_model('./saved_model/my_model.h5')
    
    """
    Method to calculate the accuracy (in percent) of the predictions made for right for each structure.
    """
    def get_per_structure_accuracy(self, y_true, y_pred):
        # The indexing for both the lists follows the numbering made 
        # for each structure in the secondary_protein_struct dictionary.

        # list to keep track of the right prediction made for each type of structure
        correct_per_structure = np.array([0,0,0])

        # list to keep track of the total number of each structure found in the data set
        total_per_structure = np.array([0,0,0])

        for i in range(len(y_true)):

            true_structure_idx = np.argmax(y_true[i])
            total_per_structure[true_structure_idx] += 1

            pred_structure_idx = np.argmax(y_pred[i])

            if true_structure_idx == pred_structure_idx:
                correct_per_structure[true_structure_idx] += 1
        
        helix_idx = secondary_protein_struct["h"]
        sheet_idx = secondary_protein_struct["e"]
        coil_idx = secondary_protein_struct["_"]

        helix_accuracy = correct_per_structure[helix_idx] / total_per_structure[helix_idx] * 100
        sheet_accuracy = correct_per_structure[sheet_idx] / total_per_structure[sheet_idx] * 100
        coil_accuracy = correct_per_structure[coil_idx] / total_per_structure[coil_idx] * 100

        return helix_accuracy, sheet_accuracy, coil_accuracy

    """
    Method to calculate the distribution (in percent) of the different types of structures found in a data set
    """
    def get_structure_dist(self, y):
        # list to keep track of the total number of each structure found in the data set
        total_per_structure = np.array([0, 0, 0])

        for struc in y:
            structure_idx = np.argmax(struc)
            total_per_structure[structure_idx] += 1

        helix_idx = secondary_protein_struct["h"]
        sheet_idx = secondary_protein_struct["e"]
        coil_idx = secondary_protein_struct["_"]

        total_structures = total_per_structure.sum()

        helix_dist = total_per_structure[helix_idx] / total_structures *  100
        sheet_dist = total_per_structure[sheet_idx] / total_structures * 100
        coil_dist = total_per_structure[coil_idx] / total_structures * 100

        return helix_dist, sheet_dist, coil_dist

