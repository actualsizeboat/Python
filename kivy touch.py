import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty(None)

    #overriding the existing functionality in the widget class
    #IE, we are overriding existing functionality
    def on_touch_down(self, touch):
        # return super().on_touch_down(touch)
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        # return super().on_touch_move(touch)
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        # return super().on_touch_up(touch)
        print("Mouse Up", touch)
        self.btn.opacity = 1.0

class TouchApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    TouchApp().run()