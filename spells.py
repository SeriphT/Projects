import random

spells = open("spells.txt","r")

spell_list = spells.readlines()
choice = random.choice(spell_list)
print(choice)

spells.close()
input()
