"""
Script containing methods to process the prediction made by the neural network
"""

import numpy as np

from dict import secondary_protein_struct


"""
Retrieves the predicted structures based on the probability distributions
gained by the prediction from the neural network.
"""
def get_structure(prediction):
    struct_result = [] 

    key_list = list(secondary_protein_struct.keys())
    val_list = list(secondary_protein_struct.values())

    for pred in prediction:
        struct_result.append(key_list[val_list.index(np.argmax(pred))])

    return struct_result


"""
Splits the protein sequence and the corresponding predicted structures into smaller segments,
in order to better display the results on the web application
"""
def split_sequences(protein_sequence, predicted_structure):

    # How many residues and structures to show for each line,
    # when represented on the webapplication
    segment_size = 70

    segments = []

    sequence_length = len(protein_sequence)

    for i in range(0, sequence_length, segment_size):
        if (i + segment_size) < sequence_length:
            # replaces '_' with 'c' for coil, to make it easier to represent
            struc = predicted_structure[i:i+segment_size]
            struc = list(map(lambda x: x.replace('_', 'c'), struc))

            segment = {
                "start": i + 1,
                "end": i + 1 + segment_size,
                "query": protein_sequence[i:i+segment_size],
                "struc": struc
            }
            segments.append(segment)
        else:
            # replaces '_' with 'c' for coil, to make it easier to represent
            struc = predicted_structure[i:sequence_length]
            struc = list(map(lambda x: x.replace('_', 'c'), struc))
            segment = {
                "start": i + 1,
                "end": sequence_length,
                "query": protein_sequence[i:sequence_length],
                "struc": struc
            }
            segments.append(segment)

    return segments
