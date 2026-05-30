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
