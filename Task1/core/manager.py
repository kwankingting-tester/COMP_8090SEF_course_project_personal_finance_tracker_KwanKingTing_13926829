import json
from models.account import Account
from models.transaction import Income, Expense

class FinanceManager:
    def __init__(self):
        self._accounts = [Account("現金錢包")]

    def add_transaction(self, acc_name: str, amount: float, category: str, is_income: bool):
        acc = next((a for a in self._accounts if a._name == acc_name), None)
        if not acc:
            acc = Account(acc_name)
            self._accounts.append(acc)

        trans = Income(amount, category) if is_income else Expense(amount, category)
        acc.add_transaction(trans)
        self.save_data()

    def show_summary(self):
        print("\n=== 記賬總覽 ===")
        for acc in self._accounts:
            print(acc)
            print("-" * 40)
            for t in acc.get_transactions()[-5:]:
                print("  ", t)
        print(f"\n總帳戶數: {len(self._accounts)}")

    def save_data(self):
        data = []
        for acc in self._accounts:
            for t in acc.get_transactions():
                data.append({
                    "account": acc._name,
                    "type": t.get_type(),
                    "amount": t._amount,
                    "category": t._category,
                    "date": t._date
                })
        with open("data/transactions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data(self):
        try:
            with open("data/transactions.json", "r", encoding="utf-8") as f:
                json.load(f)
            print("✅歷史記錄已載入")
        except:
            pass