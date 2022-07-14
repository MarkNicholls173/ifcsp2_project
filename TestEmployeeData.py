import unittest
import pandas as pd
from main import EmployeeData


class TestEmployeeData(unittest.TestCase):

    def setUp(self):
        self.ed = EmployeeData()
        self.new_record = {'FirstName': 'Tom',
                           'LastName': 'Bombadil',
                           'Position': 'Man of mystery',
                           'Salary': '88888',
                           'Email': 'tom.bombadil@manicsupplies.co.uk',
                           'HomeAddress': 'River Cottage, The Old Forest, Eriador',
                           'HomePostcode': 'ERU 5BD',
                           'HomePhone': '01234 567890',
                           'MobilePhone': '09876 543210',
                           'StartDate': '01/01/2001',
                           'ReportsTo': 'Illuvatar',
                           'EmergencyContactName': 'Goldberry',
                           'EmergencyContactPhone': '08765 678550',
                           'BirthDate': '02/05/1969'}

    def tearDown(self):
        del self.ed
        del self.new_record

    def test_load_csv_file(self):
        """does load_csv_file return a pandas dataframe"""
        self.ed.load_file("staff_data.csv")
        self.assertIsInstance(self.ed.df, pd.DataFrame)

    def test_load_xlsx_file(self):
        """does load_csv_file return a pandas dataframe"""
        self.ed.load_file("staff_data.xlsx")
        self.assertIsInstance(self.ed.df, pd.DataFrame)

    def test_get_employee(self):
        """test getting employee details based on employee id"""
        self.ed.load_file("staff_data.csv")
        employee_data = self.ed.get_employee(1000001)
        self.assertIsInstance(employee_data, pd.DataFrame)

    def test_get_new_employee_number(self):
        """test that first employee number generated is correct"""
        self.assertEqual(self.ed.get_new_employee_id(), 1000001)

    def test_add_employee(self):
        """test adding a new employee"""
        self.ed.add_employee(self.new_record)
        self.assertEqual(self.ed.df.loc[self.ed.df['EmployeeID'] == 1000001, 'FirstName'].iloc[0], 'Tom')

    def test_edit_employee(self):
        """est editing an employee based on employee id"""
        self.ed.load_file('staff_data.csv')
        self.ed.edit_employee({'EmployeeID': 1000044, 'FirstName': 'Changed'})
        self.assertEqual(self.ed.df.loc[self.ed.df['EmployeeID'] == 1000044, 'FirstName'].iloc[0], 'Changed')

    def test_delete_employee(self):
        """test deleting an employee"""
        self.ed.load_file('staff_data.csv')
        self.ed.delete_employee(1000044)
        self.assertEqual(len(self.ed.df.loc[self.ed.df['EmployeeID'] == 1000044]), 0)


if __name__ == '__main__':
    unittest.main()
