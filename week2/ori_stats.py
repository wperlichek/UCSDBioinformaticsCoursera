# Select random nucleotide in genome and use that as starting spot
# We will create a single string from it

# skew i of genome is (count of Guanine) - (count of Cytosine) in first i nucleotides of the genome
# high skew means guanine is higher and cytosine is lower (forward strand)
# low skew means guanine is lower and cytosine is higher (reverse strand)
# We expect to go from a region of high skew to low skew around the ori

# We plot skew from 0 to length of the genome. At 0 there is no skew.

# Ex string: CATGGGCATCGGCCATACGCC
import matplotlib.pyplot as plt

#1.3 Peculiar Stats
def get_genome_skew(genome):
    guanine_count = 0
    cytosine_count = 0
    skew_range = ["0"]

    for idx in range(len(genome)):
        if genome[idx] == "G":
            guanine_count = guanine_count + 1
        elif genome[idx] == "C":
            cytosine_count = cytosine_count + 1
        
        skew_range.append(guanine_count - cytosine_count)
    
    return skew_range

data = get_genome_skew("GAGCCACCGCGATA")
plt.plot(data)
plt.title("Guanine and Cytosine Difference (Skew)")
plt.xlabel("Nucleotide Position")
plt.ylabel("Skew")
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()


# We observe a sharp decrease in skew going from nucleotide 6 to nucleotide 7
# decrease in skew = cytostine is higher 
# We are at ori and at the reverse strand which the cell can replicate without okazaki fragments and thus has fewer mutations

