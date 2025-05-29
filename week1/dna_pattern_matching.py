### This is part of interactive text for week 1 in UCSD bioinformatics 1 on coursera


# Takes in DNA string, pattern, and returns count of pattern

dna_string = ""
pattern = ""
kmer_size = 0
kmer_frequency_map = {}

clumping_params = []

with open("E_coli.txt") as file:
    # kmer_size = int(file.readline().strip())
    # pattern = file.readline().strip()
    # pattern = "CTTGATCAT"
    dna_string = file.read()
    # clumping_params = file.readline().strip()

# Given a DNA string and a DNA pattern, count times pattern appears in that string
def count_dna_patterns(dna, pattern):
    if not dna or len(pattern) > len(dna):
        return 0
    pattern_count = 0
    for idx in range(len(dna)):
        if idx+len(pattern) <= len(dna) and dna[idx:idx+len(pattern)] == pattern:
            pattern_count = pattern_count + 1
    return pattern_count

# Takes in map of k-mer count map and outputs the max 
def max_map(kmerCountDict):
    max_count = 0
    for k,v in kmerCountDict.items():
        max_count = max(max_count, v)
    print("Max count: " + str(max_count))
    return max_count

# Take in an array of string print out those strings space separated 
def produce_output(strings):
    space_separated_string = " ".join(strings)
    print(str(space_separated_string))

# For all kmers size k, find those with highest frequency and return them as list
def find_most_frequent_kmers(dna, k):
    most_frequent_kmers = []
    kmer_map = {}
    
    for idx in range(len(dna)):
        if (idx + k <= len(dna)):
            kmer = dna[idx:idx+k]
            if (kmer in kmer_map):
                kmer_map[kmer] = kmer_map[kmer] + 1
            else: 
                kmer_map[kmer] = 1
    maxFreqKmer = max_map(kmer_map)

    for k,v in kmer_map.items():
        if v == maxFreqKmer:
            most_frequent_kmers.append(k)
    most_frequent_kmers.sort()
    return most_frequent_kmers

def make_kmer_map(dna, k):
    kmer_map = {}
    for idx in range(len(dna)):
        if (idx + k <= len(dna)):
            kmer = dna[idx:idx+k]
            if (kmer in kmer_map):
                kmer_map[kmer] = kmer_map[kmer] + 1
            else: 
                kmer_map[kmer] = 1    
    return kmer_map

def get_compliment(nucleotide): 
    if nucleotide == "A":
        return "T"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "G":
        return "C"
    else:
        return "G"

def find_reverse_compliment(dna):
    # Reverse the string, creating a new string
    # 5' GAC 3' -> 3' CAG 5'
    compliments = ""
    for nucleotide in rev_dna:
       compliments = compliments + get_compliment(nucleotide)
    rev_dna = compliments[::1]
    return rev_dna

# Given DNA and a pattern, find which indices are starting positions for that pattern
def find_pattern_indices_in_genome(pattern, dna):
    starting_positions = []
    for idx in range(len(dna)):
        if idx+len(pattern) <= len(dna) and dna[idx:idx+len(pattern)] == pattern:
            starting_positions.append(str(idx))
    return starting_positions

# Search genome window of size window_length for any kmers size kmer_size and count >= count
def find_clumps(dna, kmer_size, window_length, count):
    # Within a window size of 50, are there any 5-mers that have a count of 4 or more? If so, add to set list

    # Keep a string builder 
    # expand until size is window length, adding/removing from ends, keeping track in map
    # if ever any are over count, add to result set
    # when sliding window reaches size of window size, reset pointers

    # sliding window of hashes to get all kmer 
    # map has window: kmer:count
    # window is defined by len of dna/window_length
    # a kmer can be part of multiple windows though... 

    patterns = set()
    dnaLen = len(dna)

    for idx in range(dnaLen-window_length):
        currWindow = dna[idx:idx+window_length]
        kmer_map = make_kmer_map(currWindow, kmer_size) # yikes.. very inefficient
        for k,v in kmer_map.items():
            if v >= count:
                patterns.add(k)
    return patterns

# ks = int(clumping_params.split(" ")[0])
# wl = int(clumping_params.split(" ")[1])
# ct = int(clumping_params.split(" ")[2])
patterns = find_clumps(dna_string, 9, 500, 3)

print(produce_output(patterns))

# result = find_pattern_indices_in_genome(pattern, dna_string)
# cleaned_result = " ".join(result)
# print(cleaned_result)

# print("Reverse compliment 3' to 5': " + "\n" + find_reverse_compliment(dna_string))

# print(dna_string)
# print(str(kmer_size))
# mfk = find_most_frequent_kmers(dna_string, kmer_size)
# print(mfk)
# produce_output(mfk)

# kmer_frequency_map = {"GCT": 10, "CCT": 5, "AAA": 5}
# max_map(kmer_frequency_map)

# print("DNA string: " + dna_string)
# print("Pattern: " + pattern)
# result = count_dna_patterns(dna_string, pattern)
# print("Actual Result: " + str(result))

# expected_result = 0

# with open("output_4.txt") as file:
#     expected_result = int(file.readline().strip())

# if result == expected_result:
#     print("Success")
#     print("Count of pattern: " + str(result))
# else: 
#     print("Fail")
#     print("Actual Result: " + str(result))
#     print("Expected Result: " + str(expected_result))




        


    
