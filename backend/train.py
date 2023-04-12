"""
Script to train the Feed Forward Neural Network
"""

import os
from dotenv import load_dotenv

from FNN import FNN
from pre_processing import pre_proccess_data

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

    print("")

    print(" Evaluating the model ...")
    result = fnn.evaluate(X_test, y_test)
    print("test loss, test total accuracy: {:.2f}, {:.2f}%".format(result[0], result[1] * 100))

    # saves the model
    fnn.save_model()

    print("")

    print("Accuracy on training set")
    print("--------------------------")
    y_pred_train = fnn.predict(X_train)
    helix_accuracy, sheet_accuracy, coil_accuracy = fnn.get_per_structure_accuracy(y_train, y_pred_train)
    print("Alpha-helix accuracy: {:.2f}%".format(helix_accuracy))
    print("Beta-sheet accuracy: {:.2f}%".format(sheet_accuracy))
    print("Coil accuracy: {:.2f}%".format(coil_accuracy))

    print("")

    print("Accuracy on test set")
    print("--------------------------")
    y_pred_test = fnn.predict(X_test)
    helix_accuracy, sheet_accuracy, coil_accuracy = fnn.get_per_structure_accuracy(y_test, y_pred_test)
    print("Alpha-helix accuracy: {:.2f}%".format(helix_accuracy))
    print("Beta-sheet accuracy: {:.2f}%".format(sheet_accuracy))
    print("Coil accuracy: {:.2f}%".format(coil_accuracy))

    print("")

    print("Distribution of structures in the training set")
    print("------------------------------------------------")
    helix_dist, sheet_dist, coil_dist = fnn.get_structure_dist(y_train)
    print("Alpha-helix: {:.2f}%    Beta-sheet: {:.2f}%    Coil: {:.2f}%".format(helix_dist, sheet_dist, coil_dist))

    print("")

    print("Distribution of structures in the test set")
    print("------------------------------------------------")
    helix_dist, sheet_dist, coil_dist = fnn.get_structure_dist(y_test)
    print("Alpha-helix: {:.2f}%    Beta-sheet: {:.2f}%    Coil: {:.2f}%".format(helix_dist, sheet_dist, coil_dist))


if __name__ == "__main__":
   main()

