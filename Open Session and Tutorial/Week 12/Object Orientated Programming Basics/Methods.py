import random as rd
from Character import *

def enemy_attack(player):

    print("The enemy attacks!")
    
    enemy_dmg = rd.randint(0, 75)

    player_def_percent = player.defence/100
    final_dmg = enemy_dmg * player_def_percent

    print(f"The enemy hit for : {final_dmg}")

    player_hp = player.health - final_dmg
    print(f"Player health is now : {player_hp} from {player.health}!")

    player.adjust_hp(player_hp)



    



