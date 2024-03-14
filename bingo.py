import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Bingo(GridLayout):
    #Create Initialise the grid layout
    def __init__(self, **kwargs):
       
       #Call grid layout constructor
       super(Bingo, self).__init__(**kwargs)

       # Set number of columns
       self.cols = 2

       #Create a NumberGenerator Instance
       self.number = NumberGenerator()
       
       self.numSet = set()

       self.newNum = Button(text = 'New Number', font_size = 40)
       self.newNum.bind(on_press=self.press)
       self.add_widget(self.newNum)

    def press(self, instance):
        number = self.number.getRandomNum()
        
        self.add_widget(Label(text = str(number)))
        self.numSet.add(number)

class NumberGenerator():
    def __init__(self):
        self.aNum = 0
    
    def getRandomNum(self):
        return random.randint(1,90)


class MyApp(App):
    def build(self):
        return Bingo()
    
if __name__ == '__main__':
    MyApp().run()