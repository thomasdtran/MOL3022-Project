import os
from dotenv import load_dotenv

from FNN import FNN
from pre_processing import pre_proccess_data

"""
Script to train the Feed Forward Neural Network
"""

load_dotenv()

def main():
    path_train = str(os.getenv('PATH_TRAIN_DATA'))
    path_test = str(os.getenv('PATH_TEST_DATA'))

    print("Pre-proccessing data ...")

    X_train, y_train = pre_proccess_data(path_train)

    X_test, y_test = pre_proccess_data(path_test)

    print("Finished pre-proccesing data")

    # shape is (17,21)
    fnn = FNN(input_shape=(X_train.shape[1], X_train.shape[2]))
    fnn.fit(X_train, y_train)

    print("\n Evaluating the model ... \n")
    fnn.evaluate(X_test, y_test)
    fnn.save_model()


if __name__ == "__main__":
   main()


"""
Note that in the above code, we have defined a simple feedforward neural network with 3 layers 
- an input layer, a hidden layer with 128 units, another hidden layer with 64 units, 
 and an output layer with 3 units for classification. We have used the Flatten layer to convert 
 the input tensor to a 1D tensor before feeding it to the fully connected layers. 
 We have also used the categorical_crossentropy loss function and the softmax activation
function for the output layer since we have 3 classes to predict. 
 Finally, we have trained the model on the training data for 10 epochs with a batch size of 32.
 You can tweak these parameters based on your specific needs.
"""
