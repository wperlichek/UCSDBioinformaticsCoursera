from random import randint

# Input: k, list of dna strings
# Output: random kmer from each dna string
def choose_random_kmers(k, dna_strings):

    kmers = []

    for dna_string in dna_strings:
        rand_idx_min = 0
        rand_idx_max = len(dna_string)-k
        idx = randint(rand_idx_min, rand_idx_max)
        kmer = dna_string[idx:idx+k]
        kmers.append(kmer)

    return kmers

# Input: kmers 
# Output: profile for these kmers
def build_profile(kmers):
    # construct a 4 X n matrix that has the profile info
    # A .2
    # C .1
    # G .2
    # T .5
    # use pseudo counts, so add 1 to all 

    matrix = []

    for _ in range(4):
        row = []
        for idx in range(len(kmers[0])):
            row.append(0.0)
        matrix.append(row)

    for idx in range(len(kmers[0])):

        a_count = 0.0
        t_count = 0.0
        g_count = 0.0
        c_count = 0.0

        for kmer in kmers:
            if kmer[idx] == "A":
                a_count += 1.0
            elif kmer[idx] == "T":
                t_count += 1.0
            elif kmer[idx] == "G":
                g_count += 1.0
            else:
                c_count += 1.0

        # pseudocount
        a_count += 1.0
        t_count += 1.0
        g_count += 1.0
        c_count += 1.0
        revised_len = len(kmers) + 4.0

        a_percent = (a_count / revised_len)
        t_percent = (t_count / revised_len)
        g_percent = (g_count / revised_len)
        c_percent = (c_count / revised_len)
        
        matrix[0][idx] = round(a_percent, 3)
        matrix[1][idx] = round(t_percent, 3)
        matrix[2][idx] = round(g_percent, 3)
        matrix[3][idx] = round(c_percent, 3)


    return matrix

def construct_kmer_from_profile():
    return

k = 0
t = 0
dna_strings = []

with open("randoms.txt") as File:
    params = File.readline().strip().split(" ")
    k = int(params[0])
    t = int(params[1])
    dna_strings = File.readline().strip().split(" ")

random_kmers = choose_random_kmers(k, dna_strings)
#print(random_kmers)

profile = build_profile(random_kmers)

for line in profile:
    print(line)
