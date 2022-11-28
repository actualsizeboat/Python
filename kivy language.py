import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

## kivy or .kv language lets model and controller be separated?

#import widget and inherit from it to use kv file
## will need to override widget size in kv file
class MyGrid(Widget):
    ## no object property at init
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    # button always wants self and instance?????
    def btn(self):
        print(f'Name: {self.name.text} Email: {self.email.text}')
        self.name.text = ''
        self.email.text = ''


# file needs to be same as that classname that was passed on, all lower
# ex FooApp -> foo.kv
# Automagically finds the file in the same dir based on name
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__== "__main__":
    MyApp().run()