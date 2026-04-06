#  Task 2: Self-Study – Binary Heap + Heap Sort

##  Integration Plan with Task 1
In the final GUI version, Task 2 will be integrated into Task 1 to provide real-time "Top 5 Highest Spending Alerts" and sorted expense reports using the Heap.

##  Data Structure: Binary Max-Heap
Functions: Supports insert, extract_max, and heapify upward/downward operations.
Application: Powers Function 4 (Top 5 Highest Expenses).
Efficiency: Insertion complexity is O(log n), and retrieving the top 5 records is O(k log n). This is significantly faster than performing a full list scan or a complete sort.

##  Algorithm: Heap Sort
Functions: Powers Function 5 (Full Sorted Audit Report).
Efficiency: Maintains a stable time complexity of O(n log n) in all cases (best, average, and worst).

##  Algorithm Weaknesses and Limitations
Unstability: Heap Sort is an unstable sort. If multiple transactions have the exact same amount, their original relative order of entry may be changed during the sorting process.

##  Integration:
Task 2 demonstrates high robustness by functioning both as an extension of Task 1 and as a standalone module. 
The implementation ensures that the heap-based logic and the OOP data management modules interact seamlessly, regardless of whether the user starts the program from the root directory or the local sub-folder.
To run the Task 2 program independently

##  How to Run
Independent Directory Execution:
cd Task2
python main.py

Integrated Global Execution
python Task2/main.py (in root directory)
