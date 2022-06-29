import tkinter as tk
from tkinter.filedialog import asksaveasfile

import pandas as pd

from tkinter import ttk, VERTICAL, RIGHT, Y, HORIZONTAL, BOTTOM, X, filedialog, messagebox, LEFT
from pandas._config.config import OptionError


class FileHandler:
    """class to handle file operations for the gui, so file operations can be unit tested"""
    def load_csv_file(self, filename):
        """load a csv file and return a dataframe"""
        return pd.read_csv(filename)

    def load_xlsx_file(self, filename):
        """load a xlsx file and return a dataframe"""
        return pd.read_excel(filename)

    def save_xlsx_file(self, filename, df):
        """save dataframe to xlsx file"""
        writer = pd.ExcelWriter(filename)
        df.to_excel(writer, index=False)
        writer.save()

    def save_csv_file(self, filename, df):
        """save dataframe to csv file"""
        df.to_csv(filename, index=False, encoding='utf-8')


class EmployeeManagementGUI(tk.Tk):
    # constructor
    def __init__(self, file_handler):
        super().__init__()
        self.FileHandler = file_handler

        # Other variables
        font_ems = ('Helvetica', 12)
        font_ems_bold = font_ems + ('bold',)

        # Define Class Variables
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.position = tk.StringVar()
        self.salary = tk.StringVar()
        self.start_date = tk.StringVar()
        self.reports_to = tk.StringVar()
        #
        # space for rest of emp data
        #
        self.df = pd.DataFrame()
        self.file_types = (('Excel File', '*.xlsx'), ('Comma Separated Values', '*.csv'), ('All Files', '*.*'))

        # Window Setup
        self.title('Employee Management System')  # TODO can i add employee id here?
        self.geometry('900x600+600+100')

        # Widgets
        # Main Frame - data entry form
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, columnspan=4)

        # ROW 1
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

        # ROW 2
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

        # ROW 3
        # StartDate
        lbl_start_date = tk.Label(main_frame, text='Start Date', font=font_ems)
        lbl_start_date.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.text_start_date = tk.Entry(main_frame, textvariable=self.start_date, font=font_ems)
        self.text_start_date.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        # ReportsTo
        lbl_reports_to = tk.Label(main_frame, text='Reports To', font=font_ems)
        lbl_reports_to.grid(row=2, column=2, padx=10, pady=10, sticky='w')
        self.text_reports_to = tk.Entry(main_frame, textvariable=self.reports_to, font=font_ems)
        self.text_reports_to.grid(row=2, column=3, padx=10, pady=10, sticky='w')

        # TODO Email (Long)
        # TODO HomeAddress (long)
        # TODO HomePostcode
        # TODO HomePhone
        # TODO MobilePhone
        # TODO EmergencyContactName
        # TODO EmergencyContactPhone
        # TODO BirthDate

        # Button Frame
        btn_frame = tk.Frame(main_frame)
        btn_frame.grid(row=8, column=0, columnspan=4, padx=10, pady=10, sticky='w')

        # TODO Load Data Button
        tk.Button(btn_frame, command=self.load_file, text='Load Data', font=font_ems_bold,
                  width=15).grid(row=0, column=0)

        # TODO Save Data Button
        tk.Button(btn_frame, command=self.save_file, text='Save Data', font=font_ems_bold,
                  width=15).grid(row=0, column=1, padx=5)

        # TODO Add Employee Button
        tk.Button(btn_frame, command=self.add_record, text='Add Employee',  font=font_ems_bold,
                  width=15).grid(row=0, column=2, padx=5)

        # TODO Delete Employee Button
        tk.Button(btn_frame, command=self.delete_record, text='Delete Employee',  font=font_ems_bold,
                  width=15).grid(row=0, column=3, padx=5)

        # TODO Save Changes Button
        tk.Button(btn_frame, command=self.save_changes, text='Save Changes', font=font_ems_bold,
                  width=15).grid(row=0, column=4)

        # Staff List Frame
        staff_list_frame = ttk.Frame(self)
        staff_list_frame.place(x=10, y=400, width=880, height=190)

        # Staff List Style
        style = ttk.Style(self)
        style.theme_use('winnative')
        style.configure('Treeview', font=font_ems, columnwidth=10, rowheight=20,
                        background='white', fieldbackground='white')
        style.configure('Treeview.Heading', font=font_ems_bold)
        style.map('Treeview', background=[('selected', 'blue')])
        style.configure('TFrame', background='white')

        # Staff List Treeview
        self.staff_list_tv = ttk.Treeview(staff_list_frame, show='headings',
                                          columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

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
        # Bind double click to select row
        self.staff_list_tv.bind('<Double-1>', "")

    def load_file(self):
        """Load staff data from a csv file selected by the user"""
        filename = filedialog.askopenfilename(title="Select A File", filetype=self.file_types)

        if filename[-3:] == 'csv':
            try:
                self.df = self.FileHandler.load_csv_file(filename)
            except UnicodeDecodeError:
                messagebox.showerror(title="Employee Management",
                                     message="File format not recognised")
        elif filename[-4:] == "xlsx":
            try:
                self.df = self.FileHandler.load_xlsx_file(filename)
            except OptionError:
                messagebox.showerror(title="Employee Management",
                                     message="File format not recognised")

        else:
            messagebox.showerror(title="Employee Management",
                                 message="File type not supported")

        self.display_all()

    def display_all(self):
        """Display the data frame in the staff list treeview"""
        # clear the previous list
        self.staff_list_tv.delete(*self.staff_list_tv.get_children())
        # set up the headings
        self.staff_list_tv['column'] = list(self.df.columns)
        self.staff_list_tv['show'] = 'headings'
        for column in self.staff_list_tv['columns']:
            self.staff_list_tv.heading(column, text=column)
        # convert data frame to list of lists as treeview does not work with dataframes
        df_rows = self.df.to_numpy().tolist()
        # insert data in the treeview row by row
        for row in df_rows:
            self.staff_list_tv.insert('', 'end', values=row)
        # display treeview in the frame
        self.staff_list_tv.pack(side=LEFT)

    def save_file(self):
        """Function to save staff list data to a file selected by the user"""
        filename = asksaveasfile(filetypes=self.file_types, defaultextension=self.file_types)
        if filename.name[-3:] == 'csv':
            self.FileHandler.save_csv_file(filename.name, self.df)
        elif filename.name[-4:] == 'xlsx':
            self.FileHandler.save_xlsx_file(filename.name, self.df)
        else:
            messagebox.showerror(title='Employee Management System',
                                 message='Cannot save file')

    # TODO Function to add an employee
    def add_record(self):
        """Function to add a new employee"""
        pass

    # TODO Function to delete an employee record
    def delete_record(self):
        """Function to delete an employee record"""
        pass

    # TODO Function to save changes to the current record
    def save_changes(self):
        """Function to save changes to the current record"""

    # TODO function to clear boxes
    def clear_boxes(self):
        """function to clear all the boxes in the form"""
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fh = FileHandler()
    app = EmployeeManagementGUI(fh)
    app.mainloop()
