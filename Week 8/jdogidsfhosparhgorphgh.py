
pack_of_cards = ['Two of Hearts', 
                 'Two of Spades', 
                 'Two of Diamonds', 
                 'Two of Clubs', 
                 'Three of Hearts', 
                 'Three of Spades', 
                 'Three of Diamonds', 
                 'Three of Clubs', 
                 'Four of Hearts', 
                 'Four of Spades', 
                 'Four of  Diamonds',
                 'Four of Clubs', 
                 'Five of Hearts', 
                 'Five of Spades', 
                 'Five of Diamonds', 
                 'Five of Clubs', 
                 'Six of Hearts', 
                 'Six of Spades', 
                 'Six of Diamonds', 
                 'Six of Clubs', 
                 'Seven of Hearts', 
                 'Seven of Spades', 
                 'Seven of Diamonds', 
                 'Seven of Clubs', 
                 'Eight of Hearts', 
                 'Eight of Spades', 
                 'Eight of Diamonds', 
                 'Eight of Clubs', 
                 'Nine of Hearts', 
                 'Nine of Spades', 
                 'Nine of Diamonds', 
                 'Nine of Clubs', 
                 'Ten of Hearts', 
                 'Ten of Spades', 
                 'Ten of Diamonds', 
                 'Ten of Clubs', 
                 'Jack of Hearts', 
                 'Jack of Spades', 
                 'Jack of Diamonds', 
                 'Jack of Clubs', 
                 'Queen of Hearts',
                 'Queen of Spades', 
                 'Queen of Diamonds', 
                 'Queen of Clubs', 
                 'King of Hearts', 
                 'King of Spades', 
                 'King of Diamonds', 
                 'King of Clubs',
                 'Ace of Hearts',
                 'Ace of Spades', 
                 'Ace of Diamonds', 
                 'Ace of Clubs']

card_values = {'Two' : 2, 'Three' : 3, 'Four' : 4,
                'Five' : 5, 'Six' : 6, 'Seven' : 7,
                'Eight' : 8, 'Nine' : 9, 'Ten' : 10,
                'Jack' : 11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}

#Fine, I'll loop through it, only because it caught my intrest.
import random as rd

# lets store all selected cards in a list for vis
discarded = []
idx = 0

while True:
    # Find random card
    rand_card = rd.choice(pack_of_cards)
    print(f'The chosen card is : {rand_card}')

    # remove random card from list to ensure no dupes
    pack_of_cards.remove(rand_card)

    if rand_card not in pack_of_cards:
        print("Card removed")

    discarded.append(rand_card)

    print(discarded)

    choice = input("Will the next card be higher or lower (H / L)? ").upper()

    compare_last = discarded[idx-1]
    idx+=1

    rand_split = rand_card.split()
    compare_split = compare_last.split()

    randvalue = card_values[rand_split[0]]
    compvalue = card_values[compare_split[0]]

    print(randvalue)
    print(compvalue)


    if randvalue > compvalue and choice == 'H':
        print(f'Well done : {rand_card} is higher than {compare_last}')

    elif randvalue < compvalue and choice == 'L':
        print(f'Well done : {rand_card} is lower than {compare_last}')

    elif randvalue > compvalue and choice == 'L':
        print(f'Ouch, you lost {rand_card} was higher than {compare_last}')
        break

    elif randvalue < compvalue and choice == 'H':
        print(f'Ouch, you lost {rand_card} was lower than {compare_last}')
        break