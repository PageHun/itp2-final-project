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
