from heap import MaxHeap
from heapsort import heap_sort

def main():
    print("="*60)
    print("     TASK 2 DEMO - Binary Heap + Heap Sort")
    print("="*60)
    
    # 測試數據（模擬 Task 1 的支出記錄） #未來做GUI戈陣會嘗試link番兩個部份係一齊
    transactions = [
        (888.0, "2026-03-01 | 飲食"),
        (450.0, "2026-03-02 | 交通"),
        (1200.0, "2026-03-03 | 租金"),
        (65.0, "2026-03-04 | 咖啡"),
        (320.0, "2026-03-05 | 娛樂"),
        (1500.0, "2026-03-06 | 旅行"),
        (230.0, "2026-03-07 | 外賣")
    ]

    heap = MaxHeap()
    for amount, info in transactions:
        heap.insert(amount, info)

    print("\n【1】Top 5 Highest Spending (using Binary Heap):")
    for item in heap.get_top_k(5):
        print(f"   ${item[0]:.2f}  →  {item[1]}")

    print("\n【2】Full Sorted Report (using Heap Sort):")
    sorted_report = heap_sort(transactions)
    for amount, info in sorted_report:
        print(f"   ${amount:.2f}  →  {info}")

    print("\n✅ Task 2 Demo completed! (Heap + Heap Sort working independently)")

if __name__ == "__main__":
    main()
