class Account:
    def __init__(self, name: str):
        self._name = name
        self._transactions = []

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def get_balance(self) -> float:
        total = 0.0
        for t in self._transactions:
            if t.get_type() == "收入":
                total += t._amount
            else:
                total -= t._amount
        return total

    def get_transactions(self):
        return self._transactions

    def __str__(self):
        return f"帳戶: {self._name} | 結餘: ${self.get_balance():.2f}"