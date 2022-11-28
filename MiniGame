import random
import sys

## These dictionaries are used to hold the "cooldown values" for attacks.
player1 = {"Sword":2,"Spear":2,"Axe":2,"Shield":2}
player2 = {"Sword":2,"Spear":2,"Axe":2,"Shield":2}
player1hp = 5
player2hp = 5

## Game instructions below. Basically, it's rock paper scissors with more rules.
print("> Sword beats axe, axe beats spear, spear beats sword.")
print("> If you beat your opponent's move, you won't take any damage.")
print("> If you both select the same move, you'll both take damage.")
print("> Choose wisely - you can't use the same move twice in a row.")
print("> Shield will prevent all damage, but can only be used twice.")
print("> Enter q at any time to quit.")
print("> Prepare for battle!")
print("-----------------------------------")

## This while statement makes sure the game is in a valid state. If not, someone has won or lost.
while player1hp != 0 and player2hp != 0:
    
    ## These variables parse the dictionaries above and check which attacks are available to use.
    player1actions = [key for key, value in player1.items() if value >= 1]
    player2actions = [key for key, value in player2.items() if value >= 1]
    print("> Choose your move:\n",", ".join(player1actions))
    player1used = input()
    if player1used.upper() == "Q":
        sys.exit("> Coward.")
    elif player1used.capitalize() not in player1actions:
        print("> Please enter a valid move.")
    elif player1used.capitalize() in player1actions:
        ## This increments the value for each of the dictionary keys, effectively "recharging" the attack.
        player1["Sword"] += 1
        player1["Spear"] += 1
        player1["Axe"] += 1
        player2["Sword"] += 1
        player2["Spear"] += 1
        player2["Axe"] += 1
        ## Unlike other options, shield is not on a cooldown and is limited to two uses. This logic captures that.
        if "Shield" != player1used.capitalize():
            player1[player1used.capitalize()] = 0
        if "Shield" == player1used.capitalize():
            player1[player1used.capitalize()] -= 1
        player2used = random.choice(list(player2actions))
        if "Shield" != player2used.capitalize():
            player2[player2used.capitalize()] = 0
        if "Shield" == player2used.capitalize():
            player2[player2used.capitalize()] -= 1
        ## This is the actual game logic. Shield first, then scenarios where the player wins, then opponent win scenarios.
        print("> You used " + player1used + ". Your opponent used " + player2used + ".")
        if "shield" == player1used.lower() or "shield" == player2used.lower():
            print("> No Damage.")
        if "shield" != player1used.lower() and "shield" != player2used.lower() and player1used.lower() == player2used.lower():
            player1hp -= 1
            player2hp -= 1
            print("> You both hit!")
        if "sword" == player1used.lower() and "axe" == player2used.lower():
            player2hp -= 1
            print("> You hit your opponent!")
        if "spear" == player1used.lower() and "sword" == player2used.lower():
            player2hp -= 1
            print("> You hit your opponent!")
        if "axe" == player1used.lower() and "spear" == player2used.lower():
            player2hp -= 1
            print("> You hit your opponent!")
        if "axe" == player2used.lower() and "spear" == player1used.lower():
            player1hp -= 1
            print("> Your opponent hit you!")
        if "sword" == player2used.lower() and "axe" == player1used.lower():
            player1hp -= 1
            print("> Your opponent hit you!")
        if "spear" == player2used.lower() and "sword" == player1used.lower():
            player1hp -= 1
            print("Your opponent hit you!")
    print('> Current player HP: ' + str(player1hp))
    print('> Current opponent HP: ' + str(player2hp))

if player1hp == 0 and player2hp == 0:
    print(">>> It's a tie! <<<")
if player1hp > 0 and player2hp <= 0:
    print(">>> You win! <<<")
if player2hp > 0 and player1hp <= 0:
    print(">>> Your opponent wins! Your family is forever disgraced! <<<")