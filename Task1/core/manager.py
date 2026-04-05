import json
import os
import sys
from Task1.models.account import Account
from Task1.models.transaction import Income, Expense
#將Task 1 和Task 2 包在一起,令到Task 2的Heap也能在Task 1中的function使用
#用UTF-8是廢時其他系統開出bug
class FinanceManager:
    def __init__(self):
        self._accounts = [Account("Cash Wallet")]
        
        try:
            from Task2.heap import MaxExpenseHeap
            self._expense_heap = MaxExpenseHeap()
        except ImportError:
            self._expense_heap = None

    def add_transaction(self, acc_name: str, amount: float, category: str, is_income: bool):
        acc = next((a for a in self._accounts if a._name == acc_name), None)
        if not acc:
            acc = Account(acc_name)
            self._accounts.append(acc)

        trans = Income(amount, category) if is_income else Expense(amount, category)
        acc.add_transaction(trans)
        
        # 如果是支出，同步存入 Task 2 的 Heap
        if not is_income and self._expense_heap:
            self._expense_heap.insert(trans)
            
        self.save_data()

    def load_data(self):
        file_path = "data/transactions.json"
        if not os.path.exists(file_path):
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self.add_transaction(
                        item["account"], 
                        item["amount"], 
                        item["category"], 
                        item["type"] == "Income"
                    )
        except Exception as e:
            print(f"Load failed: {e}")

    def save_data(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        data = []
        for acc in self._accounts:
            for t in acc.get_transactions():
                data.append({
                    "account": acc._name,
                    "type": t.get_type(),
                    "amount": t.get_amount(),
                    "category": t.get_category(),
                    "date": t.get_date()
                })
        with open("data/transactions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def show_summary(self):
        print("\n=== Finance Summary ===") 
        for acc in self._accounts:
            print(acc)
            for t in acc.get_transactions()[-5:]:
                print("  ", t)

    
    def show_top_5_expenses(self):
        print("\n" + "-"*20)
        print(" Top 5 Highest Expenses (from Heap)")
        print("-"*20)
        if not self._expense_heap or not self._expense_heap._heap:
            print("No expenses recorded yet.")
            return
            
        top_k = self._expense_heap.get_top_k(5)
        for i, exp in enumerate(top_k, 1):
            print(f"{i}. {exp}")

    def show_sorted_expenses(self):
        print("\n" + "-"*20)
        print("Full Expense Report (Heap Sort)")
        print("-"*20)
        
        all_expenses = []
        for acc in self._accounts:
            for t in acc.get_transactions():
                if t.get_type() == "Expense":
                    all_expenses.append(t)
        
        if not all_expenses:
            print("No expenses to sort.")
            return

        from Task2.heap import MaxExpenseHeap
        sorted_list = MaxExpenseHeap.heap_sort(all_expenses)
        for exp in sorted_list:
            print(f"  {exp}")