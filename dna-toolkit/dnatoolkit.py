# DNA toolkit file

nucleotides = ['A', 'T', 'C', 'G']

# checking validity o the dna string
def validation_dna(text_seq):
    """
    input: a text sequence
    output: if all text are nucleotides, then return the sequence, \
        if one or more text are not nucleotides, then return False.
    """
    tmp_seq = text_seq.upper()
    for text in tmp_seq:
        if text not in nucleotides:
            return False
    return tmp_seq

# count number of each nucleotides
def count_nuc_frequency(dna_seq):
    tmp_freq_dict = {'A':dna_seq.count('A'),
                     'T':dna_seq.count('T'),
                     'C':dna_seq.count('C'),
                     'G':dna_seq.count('G')}
    return tmp_freq_dict