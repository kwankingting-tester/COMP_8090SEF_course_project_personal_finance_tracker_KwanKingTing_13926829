from models.transaction import Transaction

class Account:
    def __init__(self, name: str):
        self._name = name
        self._transactions = []

    def get_name(self) -> str:
        return self._name

    def add_transaction(self, transaction: Transaction):
        self._transactions.append(transaction)

    def get_balance(self) -> float:
        total = 0.0
        for t in self._transactions:
            if t.get_type() == "Income":  
                total += t.get_amount()
            else:
                total -= t.get_amount()
        return total

    def get_transactions(self):
        return self._transactions

    def __str__(self):
        return f"Account: {self._name} | Balance: ${self.get_balance():.2f}"