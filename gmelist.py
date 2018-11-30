game_list = []
while True:
    option = int(input( """
    1 - Add a game
    2 - Remove a game
    3 - Insert a game
    4 - Exit 

    make your choice 1, 2, 3, 4
    """))

    if option == 1:
        print(game_list)
        game_list.append(input("Enter the game you wish to add:\n"))
        print(game_list)

    elif option == 2:
        print(game_list)
        while True:
            rmv = input("Enter the game you wish to remove:\n")
            if rmv in game_list:
                game_list.remove(rmv)
                print(game_list)
                break
            else:
                print("Game not in list of games")
                         
    elif option == 3:
        print(game_list)
        add = input("Enter the game you wish to add:\n")
        while True:
            index = int(input("Enter the position you wnat t insert this game at:\n"))
            index -= 1
            if index < len(game_list):
                game_list.insert(index,add)
                print(game_list)
                break
            else:
                print("Invalid position")

    if option == 4:
        input("Press enter to exit")
        break
