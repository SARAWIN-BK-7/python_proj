import pandas as pd # use for read excel 
import tkinter as tk  # use for draw and close file dialog 
from tkinter import filedialog # use for open file daialog  
import sys # use for exit program 
import pickle # use for save k-nn after train 


root = tk.Tk() 
root.withdraw() 
file_path = filedialog.askopenfilename() 

if not file_path : 
    sys.exit("End Program...") 
    
# Read excel file 
df = pd.read_excel(file_path)
print(df)