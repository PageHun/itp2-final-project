import unittest
import os
from models import User, IncomeTransaction, ExpenseTransaction
from tracker import FinanceTracker

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.json"
        self.user = User("TestUser")
        self.tracker = FinanceTracker(self.user, file_path=self.test_file)
