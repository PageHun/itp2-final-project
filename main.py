from models import PremiumUser, IncomeTransaction, ExpenseTransaction
from tracker import FinanceTracker

def main():
    print("Инициализация системы Personal Finance Tracker")
    user = PremiumUser(username="Sanzhar", extra_limit=1500.0)
    tracker = FinanceTracker(user=user, file_path="data.json")
