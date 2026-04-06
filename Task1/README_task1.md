# Task 1: Personal Finance Tracker

## Problem Description
A real-life personal finance management system that helps users record income and expenses, calculate balance, and store data persistently using JSON.

## Task 1: OOP-based Personal Finance Tracker
**Problem Description:**
This is a real-life financial management system designed to help users record income and expenses, calculate balances, and maintain data persistence through JSON storage.
OOP Concepts Implementation
Abstraction: Defined a Transaction abstract base class with required abstract methods that must be implemented by subclasses.
Inheritance: Created Income and Expense classes that inherit from the Transaction base class.
Polymorphism: Subclasses override the get_type and string representation methods to provide specialized behaviors.
Encapsulation: All class attributes are protected using underscore prefixes, ensuring data integrity by restricting direct access.
Composition: The FinanceManager class manages a collection of Account and Transaction objects, forming a complete management ecosystem.

##Current Limitations
The Task 1 summary feature is designed to show only the last 5 records to maintain a clean interface. This limitation is addressed and optimized in Task 2 through advanced sorting.

