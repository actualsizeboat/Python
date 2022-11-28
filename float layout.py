import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.factory import Factory
import sys

class Start_Screen(Screen):
    pass

class Battle_Screen(Screen):
    pass

class Result_Screen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Popup():
    pass

class Widget():
    pass

kv = Builder.load_file("float.kv")

Window.size = (500, 400)
Window.minimum_width, Window.minimum_height = Window.size
Config.set('graphics', 'resizable', True)

class Foo():
    def func(arg,arg1,arg2):
        print(arg1 + arg2)
        sys.exit()

class ArenaApp(App):
    def testbtn(arg,arg1,arg2):
        ArenaApp.Foo.func(arg,arg1,arg2)
    def build(self):
        # return FloatLayout()
        return kv

if __name__ == '__main__':
    ArenaApp().run()