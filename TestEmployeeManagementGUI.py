import unittest
import pandas as pd
from main import EmployeeManagementGUI, FileHandler


class TestEmployeeManagementGUI(unittest.TestCase):

    def setUp(self):
        fh = FileHandler()
        self.app = EmployeeManagementGUI(fh)

    def tearDown(self):
        del self.app

    def test_load_csv_file(self):
        """does load_csv_file return a pandas dataframe"""
        df = self.app.FileHandler.load_csv_file("staff_data.csv")
        self.assertIsInstance(df, pd.DataFrame)

    def test_load_xlsx_file(self):
        """does load_csv_file return a pandas dataframe"""
        df = self.app.FileHandler.load_xlsx_file("staff_data.xlsx")
        self.assertIsInstance(df, pd.DataFrame)

    # def test_load_csv_file_negative(self):
    #     """does load csv file produce error when given bad file"""
    #     self.assertRaises(UnicodeDecodeError, self.app.FileHandler.load_csv_file("bad_file.csv"))

    # def test_load_xlsx_file_negative(self):
    #     """does load xlsx file produce error when given bad file"""
    #     self.assertRaises(UnicodeDecodeError, self.app.FileHandler.load_xlsx_file("bad_file.xlsx"))


if __name__ == '__main__':
    unittest.main()
