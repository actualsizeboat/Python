import random
import sys
import json

print("> Sword beats axe, axe beats spear, spear beats sword.")
print("> If you beat your opponent's move, you won't take any damage.")
print("> If you both select the same move, you'll both take damage.")
print("> Choose wisely - you can't use the same move twice in a row.")
print("> Shield will prevent all damage, but can only be used twice.")
print("> Enter q at any time to quit.")
print("> Prepare for battle!")
print("-----------------------------------")

class Records():
    def __init__(self):
        with open('records.json') as json_file:
            self.current_record = json.load(json_file)

    def increment(self,*args,val=1):
        for args in args:
            self.current_record[args] += val

    def save_records(self):
        with open('records.json','w') as json_file:
            json.dump(self.current_record, json_file)

class Player():
    def __init__(self):
        self.hp = 5
        self.actions = {"Sword":2,"Spear":2,"Axe":2,"Shield":3}

    def damage(self):
        self.hp -= 1
        if self == P1:
            running_record.increment("Damage received")
        else:
            running_record.increment("Damage dealt")

    def available_actions(self):
        return [key for key, value in self.actions.items() if value > 1]

    def use_action(self,action):
        match action:
            case "Shield":
                self.actions[action] -= 1
            case _:
                self.actions[action] = 0

    def recharge_actions(self):
        self.actions = {key:(value + 1 if key != 'Shield' else value) for (key,value) in self.actions.items()}

    def player_used(self):
        pass

def gameplay():
    while P1.hp > 0 and P2.hp > 0:
        actionloop()
        gamelogic()
    if P1.hp == 0 and P2.hp == 0:
        running_record.increment('Draws','Total')
        print(">>> It's a draw! <<<")
    if P1.hp > 0 and P2.hp <= 0:
        running_record.increment('Wins','Total')
        print(">>> You win! <<<")
    if P2.hp > 0 and P1.hp <= 0:
        running_record.increment('Losses','Total')
        print(">>> Your opponent wins! Your family is forever disgraced! <<<")

def actionloop():
    global player1used
    global player2used
    print("> Choose your move:\n",", ".join(P1.available_actions()))

    while True:
        player1used = input().capitalize()
        match player1used:
            case 'Q':
                sys.exit("> Coward.")
            case _:
                try:
                    if player1used not in P1.available_actions():
                        raise ValueError
                except:
                    print("> Choose a valid move:\n",", ".join(P1.available_actions()))
                    continue
                else:
                    break
    running_record.increment(player1used)
    P1.use_action(player1used)
    player2used = random.choice(list(P2.available_actions()))
    P2.use_action(player2used)
    P1.recharge_actions()
    P2.recharge_actions()
    
def gamelogic():
    print(f"> You used {player1used}. Your opponent used {player2used}.")
    if "Shield" == player1used or "Shield" == player2used:
        print("> No Damage.")
    if "Shield" != player1used and player1used == player2used:
        P1.damage()
        P2.damage()
        print("> You both hit!")
    match player1used:
        case 'Sword':
            if player2used == 'Spear':
                P1.damage()
                print('> Your opponent hit you!')
            if player2used == 'Axe':
                P2.damage()
                print('> You hit your opponent!')
        case 'Axe':
            if player2used == 'Sword':
                P1.damage()
                print('> Your opponent hit you!')
            if player2used == 'Spear':
                P2.damage()
                print('> You hit your opponent!')
        case 'Spear':
            if player2used == 'Axe':
                P1.damage()
                print('> Your opponent hit you!')
            if player2used == 'Sword':
                P2.damage()
                print('> You hit your opponent!')
    print(f'> Current player HP: {P1.hp}')
    print(f'> Current opponent HP: {P2.hp}')

running_record = Records()
P1 = Player()
P2 = Player()

gameplay()

while True:
    running_record.save_records()
    print("Play again? Y/N ")
    playagain = input().capitalize()
    if playagain == "N":
        sys.exit("> Coward.")
    if playagain == "Y":
        P1 = Player()
        P2 = Player()
        gameplay()
    else:
        print("Make your choice.")