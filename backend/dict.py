"""
Script containing the dictionaries used for encoding and decoding the input and output
for the neural network
"""

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
