def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance isn't defined for sequences of different lengths.")
    dist = 0
    for i in range(0, len(strand_a)):
        if strand_a[i] != strand_b[i]:
            dist += 1
    return dist