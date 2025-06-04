text = ""
k = 0
profile = []

with open("profile.txt") as File:
    text = File.readline().strip()
    k = File.readline().strip()

    for line in File:
        profile.append(line.strip().split(" "))


def most_probable_kmer_pattern(text, k, profile):

    # iterate over every substring of text from 0 to text-k length
    # for each character in the substring
    # 

    highest_probability = 0.0
    most_probable_kmer = ""

    profile_map = create_profile_map(profile, int(k))

    for idx in range(len(text-k)):
        kmer = text[idx:idx+k]
        kmer_probability = 1.0

        # for this kmer, calculate it's total probability of appearing
        # which is a product of all its nucleotides probabilities in the map 
        # 


    return

# Input: array of arrays
def create_profile_map(profile, k):
    profile_map = {}

    for idx in range(k):
        profile_map[idx] = {}
        profile_map[idx]["A"] = 0
        profile_map[idx]["C"] = 0
        profile_map[idx]["T"] = 0
        profile_map[idx]["G"] = 0

    for rowIdx in range(len(profile)):
        for colIdx in range(len(profile[rowIdx])):
            nucleotide = get_nucleotide(rowIdx)
            position = colIdx
            probability = profile[rowIdx][colIdx]
            profile_map[position][nucleotide] = probability

    return profile_map

def get_nucleotide(row):
    if row == 0:
        return "A"
    elif row == 1:
        return "C"
    elif row == 2:
        return "G"
    else:
        return "T"
