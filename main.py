import tkinter as tk
import pandas as pd
from tkinter import ttk


class EmployeeManagementGUI(tk.Tk):
    # constructor
    def __init__(self):
        super().__init__()
        

        # Define Variables
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.position = tk.StringVar()
        self.salary = tk.StringVar()

        # Window Setup
        self.title("Employee Management System") # can i add employee id here?
        self.geometry("800x600+600+100")

        # Widgets
        # Main Frame for ....
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, columnspan=4)

        # First Name
        lbl_first_name = tk.Label(main_frame, text="First Name")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = EmployeeManagementGUI()
    app.mainloop()
