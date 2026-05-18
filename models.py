import functools
from abc import ABC, abstractmethod

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Выполнение операции: {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper
