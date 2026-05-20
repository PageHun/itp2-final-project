from models import PremiumUser, IncomeTransaction, ExpenseTransaction
from tracker import FinanceTracker

def main():
    print("Инициализация системы Personal Finance Tracker")
    user = PremiumUser(username="Sanzhar", extra_limit=1500.0)
    tracker = FinanceTracker(user=user, file_path="data.json")

    try:
        tracker.add_transaction(IncomeTransaction(amount=2000.0, date="2026-05-01"))
        tracker.add_transaction(ExpenseTransaction(amount=400.0, date="2026-05-01", category="food"))
        tracker.add_transaction(ExpenseTransaction(amount=1200.0, date="2026-05-02", category="transport"))
        tracker.add_transaction(ExpenseTransaction(amount=200.0, date="2026-05-03", category="food"))
    except ValueError as e:
        print(f"Ошибка: {e}")

    tracker.save_to_file()

    print(f"Текущий баланс: {tracker.get_balance()}")
    print(f"Общий доход: {tracker.get_total_income()}")
    print(f"Общий расход: {tracker.get_total_expenses()}")
    
    print(tracker.get_category_breakdown())
    print(tracker.get_unique_categories())

if __name__ == "__main__":
    main()
