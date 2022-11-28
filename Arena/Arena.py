from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.button import Button
import random
import json

# player1used = 'none'
# player2used = 'none'

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

running_record = Records()
P1 = Player()
P2 = Player()

class Start_Screen(Screen):
    pass

class Battle_Screen(Screen):

    gameoutput = StringProperty('Choose your move!')
    gameover = StringProperty('')
    p1hp = StringProperty('5')
    p2hp = StringProperty('5')
    p1used = StringProperty('none')
    p2used = StringProperty('none')
    gameresults = StringProperty('')

    def weapon_button(self,instance):
        player2used = random.choice(list(P2.available_actions()))
        match instance:
            case self.ids.swordbtn:
                player1used = 'Sword'
            case self.ids.shieldbtn:
                player1used = 'Shield'
            case self.ids.axebtn:
                player1used = 'Axe'
            case self.ids.spearbtn:
                player1used = 'Spear'
        self.p1used = player1used.lower()
        self.p2used = player2used.lower()
        if "Shield" == player1used or "Shield" == player2used:
            self.gameoutput = 'No Damage.'
        if "Shield" != player1used and player1used == player2used:
            P1.damage()
            P2.damage()
            self.gameoutput = 'You both hit!'
        match player1used:
            case 'Sword':
                if player2used == 'Spear':
                    P1.damage()
                    self.gameoutput = 'Your opponent hit you!'
                if player2used == 'Axe':
                    P2.damage()
                    self.gameoutput ='You hit your opponent!'
            case 'Axe':
                if player2used == 'Sword':
                    P1.damage()
                    self.gameoutput = 'Your opponent hit you!'
                if player2used == 'Spear':
                    P2.damage()
                    self.gameoutput = 'You hit your opponent!'
            case 'Spear':
                if player2used == 'Axe':
                    P1.damage()
                    self.gameoutput = 'Your opponent hit you!'
                if player2used == 'Sword':
                    P2.damage()
                    self.gameoutput = 'You hit your opponent!'
        self.p1hp = str(P1.hp)
        self.p2hp = str(P2.hp)
        running_record.increment(player1used)
        P1.use_action(player1used)
        P2.use_action(player2used)
        for key, value in P1.actions.items():
            match key:
                case 'Sword':
                    if value <1:
                        self.ids.swordbtn.disabled = True
                    else:
                        self.ids.swordbtn.disabled = False
                case 'Axe':
                    if value <1:
                        self.ids.axebtn.disabled = True
                    else:
                        self.ids.axebtn.disabled = False
                case 'Spear':
                    if value <1:
                        self.ids.spearbtn.disabled = True
                    else:
                        self.ids.spearbtn.disabled = False
                case 'Shield':
                    if value <=1:
                        self.ids.shieldbtn.disabled = True
                    else:
                        self.ids.shieldbtn.disabled = False
        P1.recharge_actions()
        P2.recharge_actions()


class Result_Screen(Screen):
    pass

class ArenaApp(App):
    kv = Builder.load_file("float.kv")
    infotext = StringProperty("""> Sword beats axe, axe beats spear, spear beats sword. \n > If you beat your opponent's move, you won't take any damage. \n > If you both select the same move, you'll both take damage. \n > Choose wisely - you can't use the same move twice in a row. \n > Shield will prevent all damage, but can only be used twice.""")
    recordstext = StringProperty('')
    gameover = StringProperty('none')
    r = running_record.current_record
    recordstext = str(f'Total Games Played: {r["Total"]} \nGames Won: {r["Wins"]} \nGames Lost: {r["Losses"]} \nGames Drawn: {r["Draws"]} \nDamage dealt: {r["Damage dealt"]} \nDamage received: {r["Damage received"]} \nTimes sword chosen: {r["Sword"]} \nTimes spear chosen: {r["Spear"]} \nTimes axe chosen: {r["Axe"]} \nTimes shield chosen: {r["Shield"]} \n')

    def gamereset(self):
        global player1used
        global player2used
        global P1
        global P2
        P1 = Player()
        P2 = Player()
        player1used = "none"
        player2used = "none"
        self.gameover = 'none'

    def gamestate(self):
        if P1.hp == 0 and P2.hp == 0:
            running_record.increment('Draws','Total')
            self.gameover = 'draw'
        if P1.hp > 0 and P2.hp <= 0:
            running_record.increment('Wins','Total')
            self.gameover = 'youwon'
        if P2.hp > 0 and P1.hp <= 0:
            running_record.increment('Losses','Total')
            self.gameover = 'youlost'
        running_record.save_records()
        self.recordstext = str(f'Total Games Played: {self.r["Total"]} \nGames Won: {self.r["Wins"]} \nGames Lost: {self.r["Losses"]} \nGames Drawn: {self.r["Draws"]} \nDamage dealt: {self.r["Damage dealt"]} \nDamage received: {self.r["Damage received"]} \nTimes sword chosen: {self.r["Sword"]} \nTimes spear chosen: {self.r["Spear"]} \nTimes axe chosen: {self.r["Axe"]} \nTimes shield chosen: {self.r["Shield"]} \n')

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Start_Screen(name='start'))
        self.sm.add_widget(Battle_Screen(name='battle'))
        self.sm.add_widget(Result_Screen(name='results'))
        return self.sm

if __name__ == '__main__':
    ArenaApp().run()