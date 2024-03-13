import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initialize infite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text = 'Name: '))
        #Add Input Box
        self.name = TextInput(multiline = False)
        self.add_widget(self.name)

        # Add widgets
        self.add_widget(Label(text = 'Favourite Pizza: '))
        #Add Input Box
        self.pizza = TextInput(multiline = False)
        self.add_widget(self.pizza)

        # Add widgets
        self.add_widget(Label(text = 'Favourite colour: '))
        #Add Input Box
        self.colour = TextInput(multiline = False)
        self.add_widget(self.colour)

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()