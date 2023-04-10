import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential

"""
Feed Forward Neural Network
"""
class FNN:
    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(Flatten(input_shape=input_shape))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(3, activation='softmax'))

        self.model.compile(
            optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def fit(self, X_train, y_train, epochs=10, batch_size=32, validation_split=0.2):
        self.model.fit(X_train, y_train, epochs=epochs,
                       batch_size=batch_size, validation_split=validation_split)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test,  y_test)
    
    def save_model(self):
        self.model.save("./saved_model/my_model.h5")
    
    def load_model(self):
        self.model = tf.keras.models.load_model('./saved_model/my_model.h5')
