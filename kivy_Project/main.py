from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
import kivy

kivy.require('1.9.0')

class KVBL(BoxLayout): 
    
    pass 

class KVBoxLayoutApp(App):

    def build(self):
        return KVBL()
    
root = KVBoxLayoutApp()

root.run()