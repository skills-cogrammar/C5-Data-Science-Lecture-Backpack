import random as rd

class Character:

    def __init__(self, name="", health=100, special_attack="", style=""):

        self.name = name
        self.health = health
        self.special_attack = special_attack
        self.style = style

    def change_hp(self, new_hp):

        self.health = new_hp

    def __str__(self):

        output = f"""
Fighter Name   : {self.name}
Fighter Health : {self.health}
"""
        return output
    
#Kazuya_Mishima = Character('Kazuya', 100, "EWGF", "Mishima based Karate")
#Paul_Pheonix = Character('Paul', 100, "Death fist", "Judo")
def select_character(name):

    special = input("Enter your special attack : ")
    fighting_style = input("Enter your fighting style : ")

    player = Character(name=name, health=200, special_attack=special,
                       style=fighting_style, has_attacked=False)
    
    return player

def normal_attack(char1, char2):

    string_len = rd.randint(1,4)

    print(f"{char1.name} hits {char2.name} with a {string_len} hit combo!")

    if string_len == 1:
        dmg = rd.randint(10, 12)
        print(f"{char2.name} takes {dmg} damage!")

        new_health = char2.health - dmg
        char2.change_hp(new_health)
        print(f"{char2.name} now has {char2.health} health!")

    elif string_len == 2:
        dmg = rd.randint(15, 18)
        print(f"{char2.name} takes {dmg} damage!")

        new_health = char2.health - dmg
        char2.change_hp(new_health)
        print(f"{char2.name} now has {char2.health} health!")

    elif string_len == 3:
        dmg = rd.randint(19, 22)
        print(f"{char2.name} takes {dmg} damage!")

        new_health = char2.health - dmg
        char2.change_hp(new_health)
        print(f"{char2.name} now has {char2.health} health!")

    elif string_len == 4:
        dmg = rd.randint(23, 28)
        print(f"{char2.name} takes {dmg} damage!")

        new_health = char2.health - dmg
        char2.change_hp(new_health)
        print(f"{char2.name} now has {char2.health} health!")

def special_attack(char1, char2):

    big_dmg = rd.randint(30, 50)
    
    print(f"""
{char1.name} hits {char2.name} with their {char1.special_attack}!
    {char2.name} takes a whopping {big_dmg} damage!
""")
    
    new_health = char2.health - big_dmg
    char2.change_hp(new_health)

    print(f"{char2.name} now has {char2.health} health!")


print("Welcome to the king of iron fist!")

player1 = input("Select player 1 character : ")
player1 = select_character(player1)

player2 = input("Select player 2 character : ")
player2 = select_character(player2)


print(f"{player1.name} has the first move!")

attack = input("Normal attack or Special attack? : ").lower()

if attack == 'normal':

    normal_attack(player1, player2)

elif attack == 'special':

    special_attack(player1, player2)