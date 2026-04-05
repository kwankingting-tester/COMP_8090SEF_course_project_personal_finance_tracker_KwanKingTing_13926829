from abc import ABC, abstractmethod
#可以connect to task 1,但也可以獨立運作
try:
    # 嘗試從 Task1 啟動
    from Task1.models.transaction import Expense
except ImportError:
    # 當獨立運行 Task2 且 找不到 Task1 時，建立一個臨時的 Mock 類別，
    # 確保可以獨立運行
    class Expense:
        def __init__(self, amount: float, category: str):
            self._amount = amount
            self._category = category
        def get_amount(self) -> float: return self._amount
        def get_type(self) -> str: return "Expense"
        def __str__(self): return f"Expense: {self._category} | ${self._amount:.2f}"


class MaxExpenseHeap:
    """
    Task 2: Self-Study Data Structure - Max-Heap
    ADT Required: insert(), extract_max(), peek(), get_top_k(), build_heap()
    """
    def __init__(self):
        self._heap = []

    def _parent(self, i: int) -> int: return (i - 1) // 2
    def _left_child(self, i: int) -> int: return 2 * i + 1
    def _right_child(self, i: int) -> int: return 2 * i + 2

    def insert(self, expense: Expense):
        self._heap.append(expense)
        self._heapify_up(len(self._heap) - 1)

    def _heapify_up(self, i: int):
        parent = self._parent(i)
        if i > 0 and self._heap[i].get_amount() > self._heap[parent].get_amount():
            self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            self._heapify_up(parent)

    def extract_max(self) -> Expense:
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()
        
        max_expense = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)
        return max_expense

    def _heapify_down(self, i: int, size: int = None):
        if size is None:
            size = len(self._heap)
            
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < size and self._heap[left].get_amount() > self._heap[largest].get_amount():
            largest = left
        if right < size and self._heap[right].get_amount() > self._heap[largest].get_amount():
            largest = right

        if largest != i:
            self._heap[i], self._heap[largest] = self._heap[largest], self._heap[i]
            self._heapify_down(largest, size)

    def peek(self) -> Expense:
        return self._heap[0] if self._heap else None

    def build_heap(self, expenses: list):
        self._heap = expenses[:]
        for i in range(len(self._heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def get_top_k(self, k: int) -> list:
        """獲取前 K 個最高支出，不破壞原 Heap"""
        temp_heap = MaxExpenseHeap()
        temp_heap._heap = self._heap[:]
        
        top_k = []
        for _ in range(min(k, len(temp_heap._heap))):
            top_k.append(temp_heap.extract_max())
        return top_k

    @staticmethod
    def heap_sort(expenses: list) -> list:
        """
        Task 2 Algorithm: Heap Sort
        時間複雜度：O(n log n)
        """
        heap = MaxExpenseHeap()
        heap.build_heap(expenses)
        
        sorted_list = []
        while heap._heap:
            sorted_list.append(heap.extract_max())
        return sorted_list

# 如果你是從 Task 1 的 manager.py 去「import」它,這段就會被自動跳過,不會影響主程式
if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Running Task 2 Independently (Heap & Heap Sort Demo)")
    print("=" * 50)
    
    test_data = [
        Expense(120.0, "Food"),
        Expense(50.0, "Transport"),
        Expense(1500.0, "Rent"),
        Expense(300.0, "Entertainment"),
        Expense(45.0, "Coffee"),
        Expense(200.0, "Shopping")
    ]
    
    print("\n1. 原生未排序資料:")
    for item in test_data:
        print(f"  {item}")
        
    # 測試 Heap 排序
    print("\n2. 執行 Heap Sort (從高到低排序):")
    sorted_data = MaxExpenseHeap.heap_sort(test_data)
    for item in sorted_data:
        print(f"  {item}")
        
    # 測試 Heap 即時追蹤 Top 3
    print("\n3. 測試 Heap 即時獲取 Top 3 最高支出:")
    heap_tracker = MaxExpenseHeap()
    for item in test_data:
        heap_tracker.insert(item)
        
    top_3 = heap_tracker.get_top_k(3)
    for i, item in enumerate(top_3, 1):
        print(f"  Top {i}: {item}")
        
    print("\n✅ Task 2 獨立運行測試成功！")