import os
from dotenv import load_dotenv

import numpy as np

"""
Methods to process the data used to train the neural network
"""

load_dotenv()

# How many residues to include on each side of a residue in the sliding window.
# An offset of 8 gives a window size of 17.
win_offset = int(os.getenv('WINDOW_OFFSET'))

# stores the index of each amino acid for later use in the input layer
amino_acids_dict = {
    "A": 0,
    "R": 1,
    "N": 2,
    "D": 3,
    "C": 4,
    "Q": 5,
    "E": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "L": 10,
    "K": 11,
    "M": 12,
    "F": 13,
    "P": 14,
    "S": 15,
    "T": 16,
    "W": 17,
    "Y": 18,
    "V": 19,
    "*": 20
}

# stores the index of the two most common secondary protein structures: α-helix and β-sheet.
# if am amino acid is neither α-helix ('H') or β-sheet ('E'), then it is a random coil ('_'):
secondary_protein_struct = {"h": 0, "e": 1, "_": 2}


"""
Pre-processes either the training or testing data, and returns
the data input and target output for the nerual network
"""
def pre_proccess_data(path):
    i, o = read_data(path)
    sliding_windows, sliding_window_structures = create_all_possible_windows(i, o)
    seq, struc = create_binary_sequences(
        sliding_windows, sliding_window_structures)
    X, y = seq, struc
    return X, y


def read_data(arg_filename):

    filename = arg_filename

    # list of protein sequences
    protein_sequences = []
    #list of structures corresponding to the same indexed protein sequences
    structures = []

    # add filler data to the beginning and end in order to later read
    # the sequences with a sliding window of size 17.
    # adds an extra Z/z to ensure that the window doesnt run out of the sequence.
    protein_seq_string = "*"*(win_offset + 1)
    structure_string = "*"*(win_offset + 1)

    with open(filename, "r") as f:

        # skips the 8 first lines, as these lines are just information about the data
        for _ in range(8):
            next(f)

        for line in f:

            if "end" in line:
                protein_seq_string += "*"*(win_offset + 1)
                structure_string += "*"*(win_offset + 1)

                protein_sequences.append(protein_seq_string)
                structures.append(structure_string)

                protein_seq_string = "*"*(win_offset + 1)
                structure_string = "*"*(win_offset + 1)
            else:
                if "<>" not in line:
                    if len(line) > 2:
                        protein_seq_string += line[0]
                        structure_string += line[2]

    print("Number of proteins: {}".format(len(protein_sequences)))
    return protein_sequences, structures


"""
Creates all the subsequences for all the protein sequences made by the sliding window with
the corresponding structures for the amino acids in the middle of each sliding window subsequence.
"""


def create_all_possible_windows(protein_sequences, structures=None, training=True):

    all_sliding_windows = []

    # structure of the amino acid in the middle of the corresponding
    # indexed sliding window
    sliding_window_structures = []

    for i in range(len(protein_sequences)):
        seq = protein_sequences[i]
        for j in range(len(seq) - (win_offset * 2 + 2)):
            # index of the amino acid in the middle of the current sliding window
            mid_idx = j + win_offset + 1

            sliding_window = seq[mid_idx - win_offset: mid_idx + win_offset + 1]

            all_sliding_windows.append(sliding_window)

            if training:
                sliding_window_structures.append(structures[i][mid_idx])
    if training:
        return all_sliding_windows, sliding_window_structures
    else:
        return all_sliding_windows


def create_binary_sequences(sliding_windows, sliding_window_structures=None, training=True):

    all_binary_sequences = []

    # list of boolean vectors representing wether an amino acid i 'e', 'h' or '_'
    all_binary_structures = []

    for i in range(len(sliding_windows)):

        window = sliding_windows[i]

        binary_sequence = []

        for amino_acid in window:
            amino_acid_binary_sequence = np.zeros(
                len(amino_acids_dict)).astype(int)
            amino_acid_binary_sequence[amino_acids_dict[amino_acid]] = 1
            binary_sequence.append(amino_acid_binary_sequence)

        if len(binary_sequence) != win_offset * 2 + 1:
            continue

        all_binary_sequences.append(binary_sequence)

        if training:
            binary_structure = np.zeros(
                len(secondary_protein_struct)).astype(int)
            binary_structure[secondary_protein_struct[sliding_window_structures[i]]] = 1
            all_binary_structures.append(binary_structure)

    if training:
        return np.array(all_binary_sequences).astype(int), np.array(all_binary_structures).astype(int)
    else:
        return np.array(all_binary_sequences).astype(int)



