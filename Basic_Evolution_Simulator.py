


import random
import os

# sets up variables to begin with ancestor Genome #
ancestor_sequence = []
bases = ["A","T","C","G"]
preexisting_sequence = input("Paste a preexisting sequence here:(type none if there is none)\n")
# IF FILE IS EMPTY: add random base from bases to make random 10 base genome IF SEQUENCE IS PASTED INTO TERMINAL: ancester sequence becomes the pasted sequence#
if preexisting_sequence.lower() == "none":
    length = int(input("How long should the sequence be?\n"))
    for base in range(0,length):
        ancestor_sequence.append(bases[random.randint(0,3)])
else:
    for char in preexisting_sequence:
        ancestor_sequence.append(char)

# substitution mutation (takes out a base and replaces it with another) #
def substitution(genome):
    genome[random.randint(0,len(genome)-1)] = random.choice(bases)

# deletion mutation (removes a random base from the genome) #
def deletion(genome):
    genome.pop(random.randrange(len(genome))) 
    genome.append(random.choice(bases))

# simulates a generational mutation by picking one of the two types of mutations at random # 
def new_gen(generation):
    descendant = generation.copy()
    choice = random.randint(0,1)
    if choice  == 0:
        deletion(descendant)    
    elif choice == 1:
        substitution(descendant)
    return descendant

# asks user how many generations should be simulated #
generations = int(input("How many generations do you want to simulate?"))
generations_list = []

# simulates generational mutations accross multiple generations and saves the final generation in gen variable #
for num in range(0,generations):
    generations_list.append(num)
    # print(generations_list)

generations_list[0] = ancestor_sequence  
for gen in generations_list:
    if gen == ancestor_sequence:
        None
    else:
        gen = new_gen(old_val)
    old_val = gen   

    # BUG TESTING #
# generation_1 = ancestor_sequence.copy()
# # print(generation_1)
# substitution(generation_1)
# generation_2 = generation_1.copy()
# substitution(generation_2)
# # deletion(generation_2)

#Counts differences and displays location of differences in original and final sequences#
differences = 0
show_diff = {}
for base in range(0,len(ancestor_sequence)):
    if gen[base] != ancestor_sequence[base]:
        differences += 1
        show_diff[base + 1] = [ancestor_sequence[base],gen[base]]
    else:
        # gen[base] = "-"
        pass

#PUTS LISTS INTO DICTIONARIES SO THAT POI ARE EASILY PARSABLE FOR LATER#
headers = []
for base in range(1,len(ancestor_sequence)):
    headers.append(base)
sequences = {"Sequence": ["ancestor sequence","Final sequence"]}
for base in range(0,len(ancestor_sequence)):
        sequences[base + 1] = [ancestor_sequence[base],gen[base]]


### TURNS ANCESTOR LIST AND DESCENDANT SEQUENCE(GEN) INTO STRINGS TO BE PUT IN FASTA FORMAT#
    
str_gen = ""
for base in range(0,len(gen)):
    str_gen += ''+gen[base]

ancestor_str = ""
for base in range(0,len(ancestor_sequence)):
    ancestor_str += ''+ancestor_sequence[base]

##CHECKS TO SEE IF THERE IS ALREADY DATA IN THE TXT FILE##
f = open("my_fasta.txt", "a")
if os.path.getsize('my_fasta.txt') == 0:
    f.write(f"\n>ancestor\n{ancestor_str}\n>rand_1\n{str_gen}")
else:
    seq_name = input("what do you want to name this sequence?\n")
    f.write(f"\n>{seq_name}\n{str_gen}")
f.close()
# print(generations_list)
# print(str_gen)


