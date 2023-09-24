from tkinter import *
from tkinter import ttk 



# Create Oject 
root = Tk()


# Set root Geometry 
root.geometry('1000x500')

# Set Title for Window GUI 
root.title('Test GUI') 

label = Label(root,text="Computer ",width = 20,height=4,font=("algerian",15))
label.pack()

def data(): 
    label.config(text="Computer")
    if user_select.get() == 1:
        wl_label.config(text="Succeeded")
    elif user_select.get() == 2: 
        wl_label.config(text="Failed")
        
    
    
    
# Add dropdown box 
user_select = ttk.Combobox(root, value=["1", "2", "3", "4"])
user_select.current(0)
user_select.pack()

# Add Label, Button 
wl_label = Label(root, text="", font=("arial",10), width=50, height=4)
wl_label.pack()

button1 = Button(root, text="Spin!", font=("bell mt",10) ,command=data)
button1.pack()
button2 = Button(root, text="push", font=("bell mt",10))
button2.pack()

root.mainloop() 