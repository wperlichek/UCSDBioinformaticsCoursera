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


    return

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
print(random_kmers)