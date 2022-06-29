import unittest
import pandas as pd
from main import FileHandler


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.fh = FileHandler()

    def tearDown(self):
        del self.fh

    def test_load_csv_file(self):
        """does load_csv_file return a pandas dataframe"""
        df = self.fh.load_csv_file("staff_data.csv")
        self.assertIsInstance(df, pd.DataFrame)

    def test_load_xlsx_file(self):
        """does load_csv_file return a pandas dataframe"""
        df = self.fh.load_xlsx_file("staff_data.xlsx")
        self.assertIsInstance(df, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
