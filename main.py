import tkinter as tk
import pandas as pd
from tkinter import ttk, VERTICAL, RIGHT, Y, HORIZONTAL, BOTTOM, X


class EmployeeManagementGUI(tk.Tk):
    # constructor
    def __init__(self):
        super().__init__()

        # Other variables
        font_ems = ('Helvetica', 12)
        font_ems_bold = font_ems + ('bold',)

        # Define Class Variables
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.position = tk.StringVar()
        self.salary = tk.StringVar()

        # Window Setup
        self.title('Employee Management System')  # TODO can i add employee id here?
        self.geometry('900x600+600+100')

        # Widgets
        # Main Frame - data entry form
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, columnspan=4)

        # First Name
        lbl_first_name = tk.Label(main_frame, text='First Name', font=font_ems)
        lbl_first_name.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.text_first_name = tk.Entry(main_frame, textvariable=self.first_name, font=font_ems)
        self.text_first_name.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Last Name
        lbl_last_name = tk.Label(main_frame, text='Last Name', font=font_ems)
        lbl_last_name.grid(row=0, column=2, padx=10, pady=10, sticky='w')
        self.text_last_name = tk.Entry(main_frame, textvariable=self.last_name, font=font_ems)
        self.text_last_name.grid(row=0, column=3, padx=10, pady=10, sticky='w')

        # Position
        lbl_position = tk.Label(main_frame, text='Position', font=font_ems)
        lbl_position.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.text_position = tk.Entry(main_frame, textvariable=self.position, font=font_ems)
        self.text_position.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # Salary
        lbl_salary = tk.Label(main_frame, text='Salary', font=font_ems)
        lbl_salary.grid(row=1, column=2, padx=10, pady=10, sticky='w')
        self.text_salary = tk.Entry(main_frame, textvariable=self.salary, font=font_ems)
        self.text_salary.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        # TODO Email
        # TODO HomeAddress
        # TODO HomePostcode
        # TODO HomePhone
        # TODO MobilePhone
        # TODO StartDate
        # TODO ReportsTo
        # TODO EmergencyContactName
        # TODO EmergencyContactPhone
        # TODO BirthDate

        # Button Frame
        btn_frame = tk.Frame(main_frame)
        btn_frame.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky='w')

        # TODO Load Data Button
        tk.Button(btn_frame, command='', text='Load Data', font=font_ems_bold,
                  width=15).grid(row=0, column=0)

        # TODO Save Data Button
        tk.Button(btn_frame, command='', text='Save Data', font=font_ems_bold,
                  width=15).grid(row=0, column=1, padx=5)

        # TODO Add Employee Button
        tk.Button(btn_frame, command='', text='Add Employee',  font=font_ems_bold,
                  width=15).grid(row=0, column=2, padx=5)

        # TODO Delete Employee Button
        tk.Button(btn_frame, command='', text='Delete Employee',  font=font_ems_bold,
                  width=15).grid(row=0, column=3, padx=5)

        # TODO Save Changes Button
        tk.Button(btn_frame, command='', text='Save Changes', font=font_ems_bold,
                  width=15).grid(row=0, column=4)

        # Staff List Frame
        staff_list_frame = ttk.Frame(self)
        staff_list_frame.place(x=10, y=400, width=880, height=190)

        # Staff List Style
        style = ttk.Style(self)
        style.theme_use('winnative')
        style.configure('Treeview', font=font_ems, columnwidth=10, rowheight=10,
                        background='white', fieldbackground='white')
        style.configure('Treeview.Heading', font=font_ems_bold)
        style.map('Treeview', background=[('selected', 'blue')])
        style.configure('TFrame', background='white')

        # Staff List Treeview
        self.staff_list_tv = ttk.Treeview(staff_list_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15),
                                          show='headings')

        # Staff List Scroll Bars
        # Vertical
        sbv = ttk.Scrollbar(staff_list_frame, orient=VERTICAL)
        sbv.pack(side=RIGHT, fill=Y)
        self.staff_list_tv.config(yscrollcommand=sbv.set)
        sbv.config(command=self.staff_list_tv.yview)
        # Horizontal
        sbh = ttk.Scrollbar(staff_list_frame, orient=HORIZONTAL)
        sbh.pack(side=BOTTOM, fill=X)
        self.staff_list_tv.config(xscrollcommand=sbh.set)
        sbh.config(command=self.staff_list_tv.xview)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = EmployeeManagementGUI()
    app.mainloop()
