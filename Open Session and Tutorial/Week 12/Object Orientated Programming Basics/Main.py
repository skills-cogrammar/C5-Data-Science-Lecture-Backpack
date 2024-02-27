from Character import *
from Methods import *


username = input("Welcome adventurer! Enter your name here\n: ")
player = Character(name=username, health=100, defence=50, agility=20)

print(player)

print(f"Character created!\n{player}")
enemy_attack(player)

print(player)

enemy_attack(player)