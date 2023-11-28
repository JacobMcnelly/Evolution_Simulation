import random

# sets up variables to begin with ancestor Genome #
ancestor_sequence = []
bases = ["A","T","C","G"]

# add randome base from bases to make random 10 base genome #
for base in range(0,20):
    ancestor_sequence.append(bases[random.randint(0,3)])

# substitution mutation (takes out a base and replaces it with another) #
def substitution(genome):
    genome[random.randint(0,len(genome)-1)] = random.choice(bases)

# deletion mutation (removes a random base from the genome) #
def deletion(genome):
    genome.pop(random.randrange(len(genome))) 
    genome.append(random.choice(bases))

# simulates a generational mutation by picking one of the two tyoes of mutations at random # 
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

# prints ancestor genome and final generation genome in two lists #
print(f'''First Generation  :{ancestor_sequence}\nFinal Generation1:{gen}''')


