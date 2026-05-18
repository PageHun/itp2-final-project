import unittest
import os
from models import User, IncomeTransaction, ExpenseTransaction
from tracker import FinanceTracker

class TestFinanceTracker(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.json"
        self.user = User("TestUser")
        self.tracker = FinanceTracker(self.user, file_path=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    def test_balance_calculation(self):
        self.tracker.add_transaction(IncomeTransaction(100, "2026-05-01"))
        self.tracker.add_transaction(ExpenseTransaction(30, "2026-05-01", "food"))
        self.assertEqual(self.tracker.get_balance(), 70)
    def test_invalid_transaction_amount(self):
        with self.assertRaises(ValueError):
            IncomeTransaction(-50, "2026-05-01")

if __name__ == "__main__":
    unittest.main()
