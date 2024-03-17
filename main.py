import tkinter as tk
from tkinter import ttk
import main_menu

class App(tk.Tk):
    def __init__(self, title, dimensions):
        super().__init__()
        
        #Main Setup
        self.title(title)
        self.geometry(f'{dimensions[0]}x{dimensions[1]}')
        self.minsize(dimensions[0],dimensions[1])

        #Widgets
        self.menu = main_menu.Menu(self)

        #Main Loop
        self.mainloop()

main_windown = App('Main', (800,600))