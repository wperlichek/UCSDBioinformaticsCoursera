first_sequence = ""
second_sequence = ""


pattern = ""
dna = ""
mismatches = 0


with open ("dist.txt") as File:
    # first_sequence = File.readline().strip()
    # second_sequence = File.readline().strip()
    pattern = File.readline().strip()
    dna = File.readline().strip()
    mismatches = int(File.readline().strip())


def get_hamming_distance(str1, str2):
    hamming_distance = 0
    if len(str1) != len(str2):
        return -1
    else:
        strs_len = len(str1)
       
        for idx in range(strs_len):
            if str1[idx] != str2[idx]:
                hamming_distance = hamming_distance + 1
   
    return hamming_distance


def get_approx_matches(pattern, dna, mismatch_max):
    # scan the dna string for the pattern
    # if # differences between the string pattern <= d, this is an approx match
    # overlapping strings count. We need to evaluate substrings of length pattern.length in dna


    matches_indices = []


    for idx in range(len(dna)):
        if (idx + len(pattern) <= len(dna)):
            substr = dna[idx:idx+len(pattern)]
            hamming_distance = get_hamming_distance(substr, pattern)
            if hamming_distance <= mismatch_max:
                matches_indices.append(str(idx))


    return matches_indices


# result = get_approx_matches(pattern, dna, mismatches)    
# print(" ".join(result))


# Inputs
# Text: the genome
# Pattern: pattern to search for
# mismatches: mismatches threshold
# Description: the total number of occurrences of Pattern in Text with at most d mismatches
def get_pattern_matches_with_mismatches(text, pattern, mismatches):
    pattern_match_count = 0
    if len(pattern) > len(text):
        return 0
    for idx in range(len(text)):
        if (idx+len(pattern) <= len(text)):
            substr = text[idx:idx+len(pattern)]
            hamming_distance = get_hamming_distance(substr, pattern)
            if hamming_distance <= mismatches:
                pattern_match_count += 1
        else:
            break
    return pattern_match_count




print("Pattern " + pattern)
print("DNA " + dna)
print("Mismatches " + str(mismatches))
result = get_pattern_matches_with_mismatches(dna, pattern, mismatches)
print(str(result))




# ImmediateNeighbors(Pattern)
#     Neighborhood ← the set consisting of single string Pattern
#     for i = 1 to |Pattern|
#         symbol ← i-th nucleotide of Pattern
#         for each nucleotide x different from symbol
#             Neighbor ← Pattern with the i-th nucleotide substituted by x
#             add Neighbor to Neighborhood
#     return Neighborhood


def get_suffix_neighbors(pattern, d):


    # ACTG
    neighborhood = set()
    suffix = pattern[d:len(pattern)]


    all_nucleotides = ["A", "T", "C", "G"]
   
    for idx in range(len(suffix)):
        for idx2 in range(len(all_nucleotides)):
            neighbor = suffix[0:idx] + all_nucleotides[idx2] + suffix[idx+1:len(suffix)]
            neighborhood.add(neighbor)


    return neighborhood


def get_all_neighbors(pattern, suffixes):
    # Get patterns using the starting nucleotide from the 1st position
    all_neighbors = []
    nucleotides = ["G", "A", "C", "T"]
    for suffix in suffixes:
        all_neighbors.append(pattern[0] + suffix)
        # if the suffix matches the actual suffix from pattern, we can replace the nucleotide in pattern with the other 3
        if suffix == pattern[len(pattern)-len(suffix):len(pattern)]:
            for idx2 in range(len(nucleotides)):
                if nucleotides[idx2] != pattern[0]:
                    all_neighbors.append(nucleotides[idx2] + suffix)
    return all_neighbors


   


print("This is all assuming hamming distance = 1")
pattern = "ACG"
print("Pattern: " + pattern)
suffixes = get_suffix_neighbors(pattern, 1)
print("Suffixes: " + str(suffixes))
neighbors = get_all_neighbors(pattern, suffixes)
neighbors.remove(pattern)
print("Neighbors: " + str(neighbors))











def get_suffix_neighbors(pattern, d):


    neighborhood = set()
    suffix = pattern[d:len(pattern)]


    all_nucleotides = ["A", "T", "C", "G"]
   
    for idx in range(len(suffix)):
        for idx2 in range(len(all_nucleotides)):
            neighbor = suffix[0:idx] + all_nucleotides[idx2] + suffix[idx+1:len(suffix)]
            neighborhood.add(neighbor)


    return neighborhood


def get_all_neighbors(pattern, d):
   
    all_neighbors = []
    nucleotides = ["G", "A", "C", "T"]


    suffixes = get_suffix_neighbors(pattern, d)


    for suffix in suffixes:
        all_neighbors.append(pattern[0:d] + suffix)
        if suffix == pattern[len(pattern)-len(suffix):len(pattern)]:
            for idx2 in range(len(nucleotides)):
                if nucleotides[idx2] != pattern[0]:
                    all_neighbors.append(nucleotides[idx2] + suffix)
    return all_neighbors




def get_most_frequent_words_with_mismatches(dna, k, d):
    patterns = []
    freq_map = {}
    dna_len = len(dna)


    for idx in range(dna_len):
        if (idx+k > dna_len):
            break
        pattern = dna[idx:idx+k]
        neighbors = get_all_neighbors(pattern, d) # get all reasomable mutations, k-mer length, mutations variation up to d


        for neighbor in neighbors:
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1


    most_frequent_kmer_count = 0


    for k,v in freq_map.items():
        most_frequent_kmer_count = max(v, most_frequent_kmer_count)


    for k,v in freq_map.items():
        if v == most_frequent_kmer_count:
            patterns.append(k)


    return patterns




# Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
# Output: All most frequent k-mers with up to d mismatches in Text.


text = "GGTCGGTCGGTCCGACTCCCGCCGGTCTCCGGTCCGCCACGGGTCCGACACGACGCGCCCGCCCGCCGGTCCGACTCCCGCCACGCGCCTCCGGTCGGTCCGACGGTCCGCCCGCCCGACCGACACGACGTCCTCCCGCCACGGGTCCGACACGCGACCGCCCGCCCGCCCGCCGGTCACGCGACTCCCGACACGCGCCGGTCGGTCGGTCCGACCGCCCGACCGCCGGTCACGGGTCCGCCACGGGTCGGTCACGACGTCCCGCCGGTCTCCACGCGACACGACGACGCGACACGTCCCGCCCGCCGGTCGGTCGGTCGGTCACGCGACCGACTCCCGCCCGACGGTCCGACACGACGACGTCCGGTCGGTCGGTCACG"
k = 6
d = 2




res = get_most_frequent_words_with_mismatches(text, k, d)
print(str(res))





# TODO :: write out the problem and solve it..
# Needs a recursive implementation and mental model of the problem then it should be doable…


def get_hamming_distance(str1, str2):
    hamming_distance = 0
    if len(str1) != len(str2):
        return -1
    else:
        strs_len = len(str1)
       
        for idx in range(strs_len):
            if str1[idx] != str2[idx]:
                hamming_distance = hamming_distance + 1
   
    return hamming_distance

def get_reverse_compliment(dna):
    # ACTG
    # Compliment the single strand 
    # Reverse it
    compliment = ""

    for idx in range(len(dna)): 
        if dna[idx] == "A":
            compliment = compliment + "T"
        elif dna[idx] == "T":
            compliment = compliment + "A"
        elif dna[idx] == "G":
            compliment = compliment + "C"
        else:
            compliment = "G"
    
    reverse_compliment = compliment[::-1]
    print("DNA: " + dna)
    print("Reverse Compliment: " + reverse_compliment)
    return reverse_compliment

def neighbors(pattern, d):
    nucleotides = ["A", "T", "G", "C"]
    if d == 0:
        return {pattern}
    elif (len(pattern) == 1):
        return {"A","T","G","C"}
    else:
        neighborhood = set()
        suffix = pattern[1:len(pattern)]
        suffixNeighbors = neighbors(suffix, d)
        for suffixNeighbor in suffixNeighbors:
            if get_hamming_distance(pattern[1:len(pattern)], suffixNeighbor) < d:
                for nucleotide in nucleotides:
                    neighborhood.add(nucleotide + suffixNeighbor)
            else:
                neighborhood.add(pattern[0] + suffixNeighbor)
        return neighborhood
                
# print(str(neighbors("TATGTTGCGCAT", 2)))
# # Runtime ~O(4^k)

def frequent_words_with_mismatches_includes_reverse_compliments(pattern, k, d):
    patterns = []
    freq_map = {} 
    pattern_len = len(pattern)

    for idx in range(pattern_len-k):
        substr = pattern[idx:idx+k]
        neighborhood = neighbors(substr, d)
        reverse_compliments = []

        for neighbor in neighborhood:
            reverse_compliments.append(get_reverse_compliment(neighbor))

        neighborhood.update(reverse_compliments)

        for neighbor in neighborhood:
            if neighbor in freq_map:
                freq_map[neighbor] += 1
            else:
                freq_map[neighbor] = 1

    max_kmer_count = 0
    for k,v in freq_map.items():
        max_kmer_count = max(max_kmer_count, v)
    
    for k,v in freq_map.items():
        if v == max_kmer_count:
            patterns.append(k)

    return patterns

most_freq_kmers = frequent_words_with_mismatches_includes_reverse_compliments("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)
print(str(" ".join(most_freq_kmers)))
