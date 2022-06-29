import unittest
import pandas as pd
from main import EmployeeData


class TestEmployeeData(unittest.TestCase):

    def setUp(self):
        self.employee_data = EmployeeData()

    def tearDown(self):
        del self.employee_data

    def test_load_csv_file(self):
        """does load_csv_file return a pandas dataframe"""
        self.employee_data.load_file("staff_data.csv")
        self.assertIsInstance(self.employee_data.df, pd.DataFrame)

    def test_load_xlsx_file(self):
        """does load_csv_file return a pandas dataframe"""
        self.employee_data.load_file("staff_data.xlsx")
        self.assertIsInstance(self.employee_data.df, pd.DataFrame)

    # TODO negative tests for when load_file breaks
    # def test_load_csv_file_negative(self):
    #     """does load csv file produce error when given bad file"""
    #     self.assertRaises(UnicodeDecodeError, self.app.FileHandler.load_csv_file("bad_file.csv"))

    # def test_load_xlsx_file_negative(self):
    #     """does load xlsx file produce error when given bad file"""
    #     self.assertRaises(UnicodeDecodeError, self.app.FileHandler.load_xlsx_file("bad_file.xlsx"))

    def test_get_employee(self):
        self.employee_data.load_file("staff_data.csv")
        employee_data = self.employee_data.get_employee(1000001)
        self.assertIsInstance(employee_data, pd.DataFrame)

    # TODO tests for saving a file to csv and xlsx
    # TODO tests for getting next/new employee id
    # TODO tests for adding an employee
    # TODO tests for deleting an employee
    # TODO tests for changing employee details


if __name__ == '__main__':
    unittest.main()
