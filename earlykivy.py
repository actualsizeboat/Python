import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

## the below class will inherit from gridlayout - or any other class
class MyGrid(GridLayout):
    ## this one DOES need init'ed cuz it's making new things
    def __init__(self, **kwargs):
        
        ## creating a second grid bc it's grids all the way down - recursive grids
        self.inside = GridLayout()
        self.inside.cols = 2
        
        ## call the class constructor and set up this specific element
        super(MyGrid, self).__init__(**kwargs)
        ## the number of columns in the kivy layout - wants to fill them
        self.cols = 1
        ## method of the class
        self.inside.add_widget(Label(text='Name'))
        # call a method...
        self.name = TextInput(multiline=False)
        # ...and add it as a widget
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Last Name'))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text='Email'))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        # it's also all widgets all the way down
        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        # remember all the selfs, it's all classes
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    # creating function for button - remember to leave the init func - but do stay inside the grid class
    def pressed(self, instance):
        # creating a variable assignment for the text in the thang
        name = self.name.text
        lastname = self.lastname.text
        email = self.email.text

        print(f'{name} {lastname} {email}')
        # setting the text fields to blank after submission
        self.name.text = ''
        self.lastname.text = ''
        self.email.text = ''

# Define a class for the app and tell it to inherit from the base kivy app class
# uses the below string before App (ex: FooApp -> Foo) to name the window
class FooApp(App):
    # calling the self method to build the thing
    # doesn't need init since it's inheriting
    def build(self):
        ## this is calling the grid layout and inheriting from it
        return MyGrid()

if __name__ == "__main__":
    ## calling run method of kivy class
    FooApp().run()