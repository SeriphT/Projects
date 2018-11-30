gameList =["League of Legends", "XCom 2","Zelda Twilight Princess", "Rainbow Six Seige",
        "Stardew Valley",
        "Minecraft",
        "Plague Inc.",
        "Starcraft",
        "The Forest",
        "Kingdom Hearts 3"]

print(len(gameList))

num5game = gameList[4]
print("5th favorite game:",num5game)
indextup = gameList[1:10]
print("range of games 2-9:",indextup)

gameList +=("Doom","Final Fantasy XIII","Warframe","Riven")

print(gameList)

gameList[4] = "Starcraft"
gameList[7] = "Stardew Valley"
gameList[3] = "Kingdom Hearts 3"
gameList[9] = "Rainbow Six Seige"
print(gameList)
