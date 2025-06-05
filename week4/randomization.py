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

def construct_new_kmers(profile, dna_strings):
    
    new_kmers = []

    for dna_string in dna_strings:
        best_score_for_this_string = 0.0
        best_kmer_for_this_string = ""
        for idx in range(len(dna_string)-k):
            kmer = dna_string[idx:idx+k]
            score = get_score(profile, kmer)
            if score > best_score_for_this_string:
                best_score_for_this_string = score
                best_kmer_for_this_string = kmer

        new_kmers.append(best_kmer_for_this_string)

    return new_kmers

def get_score(profile, kmer): 
    score = 1.0
    for idx in range(len(kmer)):
        score *= profile[get_row_from_profile(kmer[idx])][idx] 
    return score

def get_row_from_profile(nucleotide):
    if nucleotide == "A":
        return 0
    elif nucleotide == "T":
        return 1
    elif nucleotide == "G":
        return 2
    else:
        return 3

def randomized_motif_search():
    
    random_kmers = choose_random_kmers(k, dna_strings)
    profile = build_profile(random_kmers)
    new_kmers_from_profile = construct_new_kmers(profile, dna_strings)

    print("Initial random set of kmers: ")

    for kmer in random_kmers:
        print(kmer)

    print("They produced this profile: ")
    for line in profile:
        print(line)

    print("We used this to produce another set of kmers from the original DNA strings, that are best per profile:")

    for new_kmer in new_kmers_from_profile:
        print(new_kmer)

    print("So for instance, this kmer: " + new_kmers_from_profile[0] + " should be the best according to profile from dna string " + dna_strings[0])
    
    return

k = 0
t = 0
dna_strings = []

with open("randoms.txt") as File:
    params = File.readline().strip().split(" ")
    k = int(params[0])
    t = int(params[1])
    dna_strings = File.readline().strip().split(" ")

randomized_motif_search()