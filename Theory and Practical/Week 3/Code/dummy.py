# enters a sentence, then make every second word uppercase and the rest 
# lowercase
count = 0
count = count + 1

new_sentence = ""
sentence = input("Please enter your sentence : ")

split_sentence = sentence.split()

# ['The', 'quick', 'brown', 'fox', 'jumps']
print(f"List : {split_sentence}")
#print(f"List Element : {split_sentence[4]}")

for i in range(len(split_sentence)):

    if i % 2 == 1:
        new_sentence += split_sentence[i].upper() + " "

    else:
        new_sentence += split_sentence[i].lower() + " "



#for count, i in enumerate(new_sentence, start=10):

#    print(f"{i} * {count} = {i * count}")


sentence = "The quick brown fox"
print(sentence.find("o"))
