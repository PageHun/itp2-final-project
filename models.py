import functools
from abc import ABC, abstractmethod

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Выполнение операции: {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper


class User:
    def __init__(self, username: str):
        self._username = username

    @property
    def username(self) -> str:
        return self._username

    def get_monthly_limit(self) -> float:
        return 50000.0


class PremiumUser(User):
    def __init__(self, username: str, extra_limit: float = 100000.0):
        super().__init__(username)
        self.extra_limit = extra_limit

    def get_monthly_limit(self) -> float:
        return self.extra_limit
        

class Transaction(ABC):
    def __init__(self, amount: float, date: str):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля.")
        self.amount = amount
        self.date = date

        @abstractmethod
    def to_dict(self) -> dict:
        pass


