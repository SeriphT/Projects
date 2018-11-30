import random
health = 100
armor = 10

attack = 15
money = 0

inventory = ["Torn cloak","Broken sheild","Rusty sword", "Potion"]

stats = ["Health:",health,"Armor:",armor,"Attack:",attack,"Money:",money]
print(stats)

for item in inventory:
    print(item)

input("Press Enter to continue")
print("You have",len(inventory),"items in your inventory")

health -= 24
print("You were attacked and lost 24 health!")
print(stats)
input()
if "Potion" in inventory:
  print("You used a potion!")
  health += 20
  inventory.remove("Potion")
  print(stats)
  print(inventory)

index = int(input("Enter index position"))
if index < len(inventory)-1 and index > -1:
    print(inventory[index])

chest = [ ]
chest_items = ["Leather armor",15, "Sword", "Hat"]

for i in range(3):
    item = random.choice(chest_items)
    chest.append(item)

print(chest)
print("The chest contains:", chest)
mun = 15
if mun in chest:
    money += 15
    chest.remove(15)
inventory += chest
print(inventory)
print(stats)
