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
    
def has_match(kmer, curr_dna, d):
    for idx in range(len(curr_dna)):
        if idx + len(kmer) <= len(curr_dna):
            curr_dna_kmer = curr_dna[idx:idx+len(kmer)]
            distance = get_hamming_distance(kmer, curr_dna_kmer)
            if distance <= d:
                return True
    return False
    
def motif_enumeration(dna, k, d):
    # (k,d) = length of kmer, mismatches allowed
    # Need to appear in every str in the collection 
    # First string: get all kmers from first string, all possibilities?
    # All strings: for all kmers gotten above, if they are in entire collection, they are (k,d) motifs
    patterns = set()
    first_str = dna[0]
    base_strs = []

    # print("First str: " + first_str)
    # print("Bases: ")

    for idx in range(len(first_str)-k+1):
        base_str = first_str[idx:idx+k]          
        base_strs.append(base_str)

    # print("------")
    # print("For each base str, get all kmers for it")

    all_kd_of_first_str = set()

    for idx in range(len(base_strs)):
        pattern = base_strs[idx]
        # print(pattern)
        base_str_neighborhood = neighbors(pattern, d)
        # print(base_str_neighborhood)
        all_kd_of_first_str.update(base_str_neighborhood)

    # print("We found these kmers for the first string, using all of its base strings:")
    # print(all_kd_of_first_str)

    # print("Now we need to check which of these exists in all the other strings")
    # print("They can be up to d apart in the other strings")
    for kmer in all_kd_of_first_str:
        matches_needed = len(dna)
        for idx in range(len(dna)):
            if has_match(kmer, dna[idx], d):
                matches_needed = matches_needed - 1
        if matches_needed == 0:
            patterns.add(kmer)

    return patterns

k = 0
d = 0
dna_strings = ""

# 3 1
# ATTTGGC TGCCTTA CGGTATC GAAAATT
with open("motifs.txt") as File:
    params = File.readline().strip()
    dna_strings = File.readline().strip()

params_as_array = params.split()
dna_strings_as_array = dna_strings.split()

patterns = motif_enumeration(dna_strings_as_array, int(params_as_array[0]), int(params_as_array[1]))

print(" ".join(patterns))