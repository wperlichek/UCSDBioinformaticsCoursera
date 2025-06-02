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

def motif_enumeration(dna, k, d):
    
    return

k = 0
d = 0
dna_strings = ""

# 3 1
# ATTTGGC TGCCTTA CGGTATC GAAAATT
with open("motifs.txt") as File:
    params = File.readline().strip()
    dna_strings = File.readline().strip()


print(params)
print(dna_strings)

params_as_array = params.split()
dna_strings_as_array = dna_strings.split()

print(params_as_array)
print(dna_strings_as_array)

motif_enumeration(params_as_array[0], params_as_array[1], dna_strings_as_array)
