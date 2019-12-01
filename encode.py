from model import vocab

chars = sorted(list(set(data_new)))
mapping = dict((c, i) for i, c in enumerate(chars))
def encode_seq(seq):
    sequences = list()
    for line in seq:
        # integer encode line
        encoded_seq = [mapping[char] for char in line]
        # store
        sequences.append(encoded_seq)
    return sequences

# encode the sequences
sequences = encode_seq(sequences)
X_tr,X_val,y_tr,y_val=vocab(mapping,sequences)