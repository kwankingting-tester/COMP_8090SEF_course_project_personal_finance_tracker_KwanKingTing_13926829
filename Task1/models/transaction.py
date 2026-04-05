from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    # Abstract class - Demonstrate Abstraction
    def __init__(self, amount: float, category: str, date: str = None):
        self._amount = amount
        self._category = category
        self._date = date or datetime.now().strftime("%Y-%m-%d %H:%M")

    @abstractmethod
    def get_type(self) -> str:
        pass
    
    # Encapsulation: Providing getters for private attributes
    def get_amount(self) -> float:
        return self._amount

    def get_category(self) -> str:
        return self._category
        
    def get_date(self) -> str:
        return self._date

    def __str__(self):
        return f"{self._date} | {self.get_type():<7} | {self._category:<10} | ${self._amount:.2f}"

class Income(Transaction):
    def get_type(self):
        return "Income" 

class Expense(Transaction):
    def get_type(self):
        return "Expense"