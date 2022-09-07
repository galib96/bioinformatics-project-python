from dnatoolkit import *
import random

# generate random DNA sequence
seq = ''.join([random.choice(nucleotides) for i in range(50)])

# validating DNA sequence
val_seq = validation_dna(seq)

# counting number of nucleotides
print(count_nuc_frequency(val_seq))