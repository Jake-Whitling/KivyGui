import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Bingo(GridLayout):
    #Create Initialise the grid layout
    
    # Create a press button function
    def press(self, instance):
        number = self.number.getRandomNum()

        while number in self.numSet:
            number = self.number.getRandomNum()
        
        self.numSet.add(int(number))
        self.top_grid.add_widget(Label(text = str(number)))

    # Create a printLsit function to print off all numbers that have been added
    def printList(self, instance):
        self.add_widget(Label(text = str(sorted(self.numSet))))
        print(self.numSet)

    def __init__(self, **kwargs):
       
       #Call grid layout constructor
       super(Bingo, self).__init__(**kwargs)

       # Set number of columns
       self.cols = 1

       # Create and add top grid
       self.top_grid = GridLayout()
       self.top_grid.cols = 10
       
       self.top_grid.add_widget(Label(text = "Numbers list"))
       self.add_widget(self.top_grid)

       #Create a NumberGenerator Instance
       self.number = NumberGenerator()
       self.numSet = set()
       
       # Add the bottom New Number button
       self.newNum = Button(text = 'New Number', font_size = 40)
       self.newNum.bind(on_press=self.press)
       self.add_widget(self.newNum)

       # Add the Print set button
       self.submit = Button(text = "Print Set", font_size = 40)
       self.submit.bind(on_press = self.printList)
       self.add_widget(self.submit)


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