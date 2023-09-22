"""
    Mr. Sarawin Buakaew 
    Ohm's Laws or Electrical Triangle 
    
    V : Voltage 
    I : Current 
    R : Resistance  
     
    V = I x R 
    I = V / R 
    R = V / I 
        
"""
import math 

class OhmsLaws():
    
    def __init__(self): 
        self.V = None 
        self.I = None  
        self.R = None
        
    
    def Voltage(self): 
        x = int(input("Please enter The Current : "))
        y = int(input("Please enter The Resistance ")) 
        
        # result = math.multiply(x,y) 
        self.V = x * y 
        
        return self.V 
    
    def Current(self):
        x = int(input("Please enter The Voltage : "))
        y = int(input("Please enter The Resistance "))

        self.I = x/y
        
        return self.I 
    
    def Resistance(self):
        x = int(input("Please enter The Voltage : "))
        y = int(input("Please enter The Current : "))
     
        self.R = x / y
        
        return self.R 
     
if __name__ == "__main__": 
    Ohm = OhmsLaws()
    print("Welcome to OhmsLaws Please enter number : \t\n"+
          "Voltage\t\n"+
          "Current\t\n"+
          "Resistance\t\n"
            )
    v = Ohm.Voltage()
    c = Ohm.Current()
    r = Ohm.Resistance()
    print(f"voltage : {v}")
    print(f"Current : {c}")
    print(f"Resistance : {r}")