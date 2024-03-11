# add prefix to a word v
# add prefixes to a group of words
# remove a suffix from a word
# convert adjective to verb

def verbalise(text, idx):
    
    split_text = text.split()
    
    return split_text[idx] + 'en'

print(verbalise('It got dark as the sun set.', 2))


def add_prefix(text):
    
    prefixes = ['un', 're', 'dis', 'mis', 'sub']
    # add prefix to word
    while True:
        fix = input("Please enter the prefix, you'd like to add : ")
    
        if fix in prefixes:
        
            idx = prefixes.index(fix)
            return prefixes[idx] + text
            
        else:
            print('Not a prefix')
            continue
    
def add_prefixes(texts):
    
    fixedwords = []
    prefixes = ['un', 're', 'dis', 'mis', 'sub']
    # add prefix to word
    while True:
        fix = input("Please enter the prefix, you'd like to add : ")

        if fix in prefixes:
        
            idx = prefixes.index(fix)
            
            for text in texts:
                fixedwords.append(prefixes[idx] + text)
                
            return fixedwords
            
        else:
            print('Not a prefix')
            continue
        
        

def remove_suffix_ness(word):
    new_word = word[:-4]
    if new_word[-1] == "i":
        new_word = new_word[:-1] + "y"

    return new_word

# User input and running function to remove suffix
while True: 
    ness_word = input("\nEnter a word that has the 'ness' suffix: ")
    if "ness" in ness_word:
        new_word = remove_suffix_ness(ness_word)
        break
    else:
        print("\nThe word you entered does not contain the suffix 'ness'.")
    
    
print(f"\n\nAfter removing the suffix your new word is: '{new_word}'.\n\n")

    
    