from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

# Windowmanager is transitions between windows
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("screens.kv")

class ScreensApp(App):
    def build(self):
        return kv






if __name__ == "__main__":
    ScreensApp().run()