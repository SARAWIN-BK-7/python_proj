from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput

# Control the Environment 
import os 
os.environ["KIVY_TEXT"] = 'pil'
import kivy 


class LoginScreen(GridLayout): 
    
    def __init__(self, **kawarge): 
        super(LoginScreen, self).__init__(**kawarge)
        self.cols=1
        # self.add_widget(Label(text="User Name")) 
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username) 
        # self.add_widget(Label(text="Password"))
        # self.password = TextInput(password=True, multiline=False) 
        
        self.add_widget(Label(text="Sarawin Buakaew"))

        
class MyApp(App):    
    
    def build(self):
        return LoginScreen()
    
if __name__ == "__main__": 
    MyApp().run() 