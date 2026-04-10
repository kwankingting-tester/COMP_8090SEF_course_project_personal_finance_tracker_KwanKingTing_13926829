# COMP8090SEF Course Project - Personal Finance Tracker & Self-Study

Student: Kwan King Ting
Student No: 13926829 

## Project Structure:
Task1 Folder: Contains the primary OOP infrastructure, implementing Encapsulation, Inheritance, Polymorphism, and Abstraction.
Task2 Folder: Contains the self-study implementation of the Binary Heap and Heap Sort algorithms.
transactions.json: A centralized database file shared by both tasks to ensure data consistency across the application.

## This repository contains both tasks for the course project:
**Task 1: OOP-based Application**
Personal Finance Tracker – A real-life expense and income management system.  
Fully implements all OOP concepts taught in the course (Abstraction, Inheritance, Polymorphism, Encapsulation) using multiple modules.

Location: /Task1/
Detailed README:[Task1/README_task1.md](Task1/README_task1.md)
How to run:
cd task1  
python main.py

### Project Demonstration
Here is a Introduction video of the Task1:
(The video below is compressed for GitHub. For better quality, please refer to the Google Drive link provided in my OLE and Project Report.)
https://github.com/user-attachments/assets/c93a2e22-20cf-4f86-b464-ea74d1ce152c



**Task 2: Self-Study on New Data Structure & Algorithm**
The Heap maintains real-time Top 5 highest spending alerts, while Heap Sort generates sorted monthly reports.  
This makes the finance system intelligent — after every new transaction in Task 1, Task 2 automatically updates priority spending data.
Unlike separate scripts, this project integrates Task 2 directly into the Task 1 core engine. 
Task 1 provides the Object-Oriented infrastructure (Accounts, Transactions, Data Persistence)
Task 2 enhances the system with a Binary Max-Heap to provide real-time "Top 5 Spending Alerts" and Heap Sort for analytical reports

Location: /Task2/
Detailed README: [Task2/README_task2.md](Task2/README_task2.md)
How to run(Global)(To run Task 2 from this root directory and include Task 1 data:): 
python Task2/main.py

### Project Demonstration
(The video below is compressed for GitHub. For better quality, please refer to the Google Drive link provided in my OLE and Project Report.)
Here is a Introduction video of the Task2:
https://github.com/user-attachments/assets/bb7030a5-e3b5-4126-b6c8-e8818f6c0212





