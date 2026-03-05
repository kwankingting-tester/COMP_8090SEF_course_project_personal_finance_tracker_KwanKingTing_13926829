from heap import MaxHeap
from heapsort import heap_sort

def main():
    print("="*60)
    print("     TASK 2 DEMO - Binary Heap + Heap Sort")
    print("="*60)
    
    # Test data (simulating Task 1 expense records)
    transactions = [
        (888.0, "2026-03-01 | Food"),
        (450.0, "2026-03-02 | Transport"),
        (1200.0, "2026-03-03 | Rent"),
        (65.0, "2026-03-04 | Coffee"),
        (320.0, "2026-03-05 | Entertainment"),
        (1500.0, "2026-03-06 | Travel"),
        (230.0, "2026-03-07 | Takeout")
    ]

    heap = MaxHeap()
    for amount, info in transactions:
        heap.insert(amount, info)

    print("\n[1] Top 5 Highest Spending (using Binary Heap):")
    for item in heap.get_top_k(5):
        print(f"   ${item[0]:.2f}  →  {item[1]}")

    print("\n[2] Full Sorted Report (using Heap Sort):")
    sorted_report = heap_sort(transactions)
    for amount, info in sorted_report:
        print(f"   ${amount:.2f}  →  {info}")

    print("\n✅ Task 2 Demo completed! (Heap + Heap Sort working independently)")

if __name__ == "__main__":
    main()