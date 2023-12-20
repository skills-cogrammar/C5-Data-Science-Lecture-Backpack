dna_sequence = 'atcgctagctag'
upper_sequence = dna_sequence.upper()
replace_sequence = upper_sequence.replace('A', 'T')

print(f"""
Original : {dna_sequence}
Upper : {upper_sequence}
Replaced : {replace_sequence}
    """)

genetic_marker = 'TCGA'

if genetic_marker in upper_sequence:
    
    print(f"Genetic marker located : {genetic_marker}")

user = input("Select the letter you would like to split off : ").upper()
segment = upper_sequence.split(user)
print(f"Segments split by {user} : {segment}")

trait_sequence = 'TAG'

if trait_sequence in segment:
    
    print(f"Trait for blue eyes {trait_sequence} likely present")