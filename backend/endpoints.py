import os
from dotenv import load_dotenv
from FNN import FNN
from pre_processing import create_all_possible_windows, create_binary_sequences
from post_processing import get_structure, split_sequences

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

"""
Script containing the RESTful API for the prediction 
of secondary structures
"""

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

fnn = FNN(input_shape=(17,21))

#loads pre-trained feed forward neural network model
fnn.load_model()

@app.route("/prediction", methods=['POST'])
@cross_origin()
def predict():
    data = request.get_json()

    # adds filler characters for the window sliding
    protein_sequence = ["*********" + data["proteinSequence"] + "*********"]

    sliding_windows = create_all_possible_windows(protein_sequence, training=False)
    binary_sequences = create_binary_sequences(sliding_windows, training=False)

    prediction = fnn.predict(binary_sequences)

    predicted_structure = get_structure(prediction)

    segments = split_sequences(data["proteinSequence"], predicted_structure)

    return jsonify(segments)


