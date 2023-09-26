from tkinter import *
from tkinter.ttk import *
# Create Oject 
root = Tk()
style = Style()



# Set root Geometry 
root.geometry('1000x500')

# Set Title for Window GUI 
root.title('GUI')

# Set icon  
# root.iconbitmap(r'D:\python_proj\image\python_button_icon_151925.ico')

# Style Button 
style.configure('W.TButton1', font=
                ('calibri',10,'bold','underline'),
                foreground='red'
                )

def ActionButton():
    
    return 

btn1 = Button(root, text="Click me", style="W.TButton")
btn1.grid(row=0, column=3, padx=100)
# btn1.pack(side='left')

btn2 = Button(text="Ok!", style="W.TButton")
btn2.grid(row=1, column=3, padx=100)
# btn2.pack(side='right')

root.mainloop() 