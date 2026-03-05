from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    """Abstract class - Demonstrate Abstraction"""
    def __init__(self, amount: float, category: str, date: str = None):
        self._amount = amount
        self._category = category
        self._date = date or datetime.now().strftime("%Y-%m-%d %H:%M")

    @abstractmethod
    def get_type(self) -> str:
        pass

    def __str__(self):
        return f"{self._date} | {self.get_type()} | {self._category} | ${self._amount:.2f}"

class Income(Transaction):
    def get_type(self):
        return "Income" 

    def __str__(self):
        return super().__str__()

class Expense(Transaction):
    def get_type(self):
        return "Expense"  

    def __str__(self):
        return super().__str__()
