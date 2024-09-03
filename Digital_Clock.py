import tkinter as tk
from time import strftime       #strftime is use forward time and date change as per our choice

#to make root window to display the time and date 

root = tk.Tk()      #we create object name is root 
root.title("Digital Clock") 

#Create a funtion for time 
def time():  
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font =('calibri' , 50, 'bold'), background='blue',foreground='black')
label.pack(anchor='center')

time()

root.mainloop()