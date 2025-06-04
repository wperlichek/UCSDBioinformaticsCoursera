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

# params_as_array = params.split()
# dna_strings_as_array = dna_strings.split()

# patterns = motif_enumeration(dna_strings_as_array, int(params_as_array[0]), int(params_as_array[1]))

# print(" ".join(patterns))


# k = kmer size integer
# dna_strings = collection of dna strings
def median_string(k, dna_strings):

    # Below "grand total" is the grand total for a kmer_pattern to dna_strings score
    # The lowest score possible taking a k_mer, iterating over every kmer every dna string in dna strings
    # We must match one per dna string
    # We return the kmer which produced the lowest grand total

    # for each kmer_pattern in kmer_pattern_from_possibilities
        # for each dna_string in dna_strings
            # for each kmer_pattern_in_dna_string in dna_string
                # grand_total += lowest total of distance kmer_pattern_in_dna_string to kmer_pattern_from_possibilities
        # if grand_total < best grand total found, record new grand total and save pattern

    # n = len of kmer_pattern_from_possibilities
    # l = len of dna_strings
    # m = len of dna_string - k 
    # Time Complexity: O(n*l*m)..

    # TODO :: 
    # How to generate kmer_pattern_from_possibilities?
    # Do we know that this pattern must be derived from an existing string? Must it exist in some string?
    # Or do we take k size and make all possibilities for it, and then search those?
    # But above is like 4^k 4 choose k which is... really bad if say k is 10. It's ~1 million strings, doable and accurate
    # We want to generate kmer_pattern_from_possibilities outside of the nested loops


    
    # for each kmer_pattern in kmer_pattern_from_possibilities
        # for each dna_string in dna_strings
            # for each kmer_pattern_in_dna_string in dna_string
                # grand_total += lowest total of distance kmer_pattern_in_dna_string to kmer_pattern_from_possibilities
        # if grand_total < best grand total found, record new grand total and save pattern

    kmer_pattern_from_possibilities = generate_kmer_possibilities(k, "", [])
    best_pattern = ""
    best_total_from_all_kmer_patterns = 2**31-1

    for kmer_pattern in kmer_pattern_from_possibilities:

        grand_total_this_kmer_pattern = 0

        for dna_string in dna_strings:
            lowest_found_this_dna_string = 2**31-1
            for idx in range(len(dna_string)):
                if idx+k <= len(dna_string):
                    lowest_found_this_dna_string = min(lowest_found_this_dna_string, get_hamming_distance(dna_string[idx:idx+k], kmer_pattern))
            grand_total_this_kmer_pattern += lowest_found_this_dna_string
        
        if (grand_total_this_kmer_pattern < best_total_from_all_kmer_patterns):
            best_total_from_all_kmer_patterns = grand_total_this_kmer_pattern
            best_pattern = kmer_pattern
            
    return best_pattern # the median string

# n = 3
# 4 choose 3
# Time Complexity: O(4^3)
def generate_kmer_possibilities(n, curr_string, all_possibilities):
    if (len(curr_string) < n):
        nucleotides = ["G", "C", "T", "A"]
        for nucleotide in nucleotides:
            generate_kmer_possibilities(n, curr_string + nucleotide, all_possibilities)
    else:
        all_possibilities.append(curr_string)
    
    return all_possibilities

# result = generate_kmer_possibilities(3, "", [])
# print(len(result))

# k = 0
# dna_strings = []

# with open("kmer_motifs.txt") as File:
#     k = File.readline().strip()
#     for line in File:
#         dna_strings.append(line.strip())

# print(k)
# print(dna_strings)

# print(median_string(int(k), dna_strings))


def median_string_crude(pattern, dna_strings):
    total_distance = 0
    k = len(pattern)
    
    for dna_string in dna_strings:
        min_hamming_distance_found = 2**31-1
        for idx in range(len(dna_string)-k):
            dna_string_pattern = dna_string[idx:idx+k]
            hamming_distance = get_hamming_distance(dna_string_pattern, pattern)
            if hamming_distance < min_hamming_distance_found:
                min_hamming_distance_found = hamming_distance
        total_distance += min_hamming_distance_found
            
    return total_distance


pattern = ""
dna_strings = []

with open("median_string.txt") as File: 
    pattern = File.readline().strip()
    dna_strings = File.readline().strip().split(" ")

res = median_string_crude(pattern, dna_strings)
print(str(res))