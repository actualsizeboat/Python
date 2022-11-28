import random
import sys

## These dictionaries are used to hold the "cooldown values" for attacks.
player1 = {"Sword":2,"Spear":2,"Axe":2,"Shield":2}
player2 = {"Sword":2,"Spear":2,"Axe":2,"Shield":2}
player1hp = 5
player2hp = 5

## Game instructions below. It's basically rock paper scissors with more rules.
print("> Sword beats axe, axe beats spear, spear beats sword.")
print("> If you beat your opponent's move, you won't take any damage.")
print("> If you both select the same move, you'll both take damage.")
print("> Choose wisely - you can't use the same move twice in a row.")
print("> Shield will prevent all damage, but can only be used twice.")
print("> Enter q at any time to quit.")
print("> Prepare for battle!")
print("-----------------------------------")

## This while statement makes sure the game is in a valid state. If not, someone has won or lost.
while player1hp > 0 and player2hp > 0:
    
    ## These variables parse the dictionaries above and check which attacks are available to use.
    player1actions = [key for key, value in player1.items() if value >= 1]
    player2actions = [key for key, value in player2.items() if value >= 1]
    print("> Choose your move:\n",", ".join(player1actions))
    player1used = input()
    player1used = player1used.capitalize()
    if player1used == "Q":
        sys.exit("> Coward.")
    elif player1used not in player1actions:
        print("> Please enter a valid move.")
    elif player1used in player1actions:
        
        ## This increments the value for each of the dictionary keys except shield, effectively "recharging" the actions.
        player1 = {key:(value + 1 if key != 'Shield' else value) for (key,value) in player1.items()}
        player2 = {key:(value + 1 if key != 'Shield' else value) for (key,value) in player2.items()}
        
        player2used = random.choice(list(player2actions))

        ##This sets the value for the chosen action.
        match player1used:
            case "Shield":
                player1[player1used] -= 1
            case _:
                player1[player1used] = 0
        match player2used:
            case "Shield":
                player2[player2used] -= 1
            case _:
                player2[player2used] = 0
        
        ## This is the actual game logic.
        print(f"> You used {player1used}. Your opponent used {player2used}.")
        if "Shield" == player1used or "Shield" == player2used:
            print("> No Damage.")
        if "Shield" != player1used and player1used == player2used:
            player1hp -= 1
            player2hp -= 1
            print("> You both hit!")
        match player1used:
            case 'Sword':
                if player2used == 'Spear':
                    player1hp -= 1
                    
                    print('> Your opponent hit you!')
                if player2used == 'Axe':
                    player2hp -= 1
                    print('> You hit your opponent!')
            case 'Axe':
                if player2used == 'Sword':
                    player1hp -= 1
                    print('> Your opponent hit you!')
                if player2used == 'Spear':
                    player2hp -= 1
                    print('> You hit your opponent!')
            case 'Spear':
                if player2used == 'Axe':
                    player1hp -= 1
                    print('> Your opponent hit you!')
                if player2used == 'Sword':
                    player2hp -= 1
                    print('> You hit your opponent!')
    print(f'> Current player HP: {player1hp}')
    print(f'> Current opponent HP: {player2hp}')

if player1hp == 0 and player2hp == 0:
    print(">>> It's a tie! <<<")
if player1hp > 0 and player2hp <= 0:
    print(">>> You win! <<<")
if player2hp > 0 and player1hp <= 0:
    print(">>> Your opponent wins! Your family is forever disgraced! <<<")