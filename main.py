import tkinter as tk
import pandas as pd
from tkinter import ttk


class EmployeeManagementGUI(tk.Tk):
    # constructor
    def __init__(self):
        super().__init__()

        font_helv = ('Helvetica', 12)


        # Define Variables
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.position = tk.StringVar()
        self.salary = tk.StringVar()

        # Window Setup
        self.title('Employee Management System')  # can i add employee id here?
        self.geometry('800x600+600+100')

        # Widgets
        # Main Frame for ....
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, columnspan=4)

        # First Name
        lbl_first_name = tk.Label(main_frame, text='First Name', font=font_helv)
        lbl_first_name.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.text_first_name = tk.Entry(main_frame, textvariable=self.first_name, font=font_helv)
        self.text_first_name.grid(row=0, column=1, padx=10, pady=10, sticky='w')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = EmployeeManagementGUI()
    app.mainloop()
