from kivy.core.text import LabelBase 
from kivy.utils import rgba 
from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.core.window import Window 
Window.size = (310, 580)

kv = """





"""

class YourAppApp(MDApp): 
    
    def build(self):
        return Builder.load_string(kv)
    

if __name__ == "__main__": 
    
    