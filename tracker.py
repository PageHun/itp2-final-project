import json
import os
from typing import List, Dict, Generator
from models import Transaction, IncomeTransaction, ExpenseTransaction, User, log_action

class FinanceTracker:
    def __init__(self, user: User, file_path: str = "data.json"):
        self.user = user
        self.file_path = file_path
        self.transactions: List[Transaction] = []
        self.load_from_file()

    @log_action
    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
        self.check_overspending(transaction)

    def check_overspending(self, transaction: Transaction) -> None:
        if isinstance(transaction, ExpenseTransaction):
            total_expenses = self.get_total_expenses()
            limit = self.user.get_monthly_limit()
            if total_expenses > limit:
                print(f"ВНИМАНИЕ: Превышен лимит пользователя {self.user.username}!")

    def get_expenses_generator(self) -> Generator[ExpenseTransaction, None, None]:
        for tx in self.transactions:
            if isinstance(tx, ExpenseTransaction):
                yield tx

    def get_total_expenses(self) -> float:
        expenses = filter(lambda tx: isinstance(tx, ExpenseTransaction), self.transactions)
        return sum(tx.amount for tx in expenses)

    def get_total_income(self) -> float:
        incomes = filter(lambda tx: isinstance(tx, IncomeTransaction), self.transactions)
        return sum(tx.amount for tx in incomes)

    def get_balance(self) -> float:
        return self.get_total_income() - self.get_total_expenses()

    def get_category_breakdown(self) -> Dict[str, float]:
        breakdown = {}
        for expense in self.get_expenses_generator():
            breakdown[expense.category] = breakdown.get(expense.category, 0.0) + expense.amount
        return breakdown

    def get_unique_categories(self) -> set:
        return {tx.category for tx in self.transactions if isinstance(tx, ExpenseTransaction)}
