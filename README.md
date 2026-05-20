# Personal Finance Tracker

## Project Description
This project is a comprehensive console-based Personal Finance Tracker designed to simulate real-world financial management. The application provides key functionalities for tracking income and expenses, aggregating analytical breakdowns by category, tracking user-specific budgets, and detecting budget overspending.

The primary objective of this development is to demonstrate a deep understanding of core software engineering principles, proper object-oriented programming (OOP) design, advanced Python features, memory optimization, and robust error handling.

---

## Group members:
  1. Sarsenbekov Sanzhar
  2. Zamanbek Berdigali
  3. Alnur Kulan
  4. Korganbek Kyanyshbek

---

## Technical and Architectural Justifications

### 1. Object-Oriented Programming (OOP) & Design Patterns
* **Encapsulation:** In the `User` class, the username is hidden using a protected attribute (`self._username`) and exposed via a read-only property wrapper (`@property`). This prevents arbitrary mutation from external modules.
* **Inheritance & Polymorphism:** The `PremiumUser` class inherits from `User` and overrides the `get_monthly_limit()` method. This allows the tracking engine to compute spending thresholds dynamically without knowing the exact runtime subclass of the user.
* **Abstraction:** The base `Transaction` class inherits from `abc.ABC` and defines an abstract method `to_dict()`. The concrete subclasses `IncomeTransaction` and `ExpenseTransaction` implement this method to encapsulate their serialization logic, allowing polymorphic data processing during file persistence.

### 2. Advanced Python Features & Memory Optimization
* **Custom Decorators:** The `log_action` utility uses `functools.wraps` to preserve function metadata while decoupling cross-cutting logging concerns from the core business domain logic.
* **Memory-Efficient Generators:** To handle large histories of data without high memory overhead, `tracker.py` utilizes the `yield` keyword within `get_expenses_generator()`. This evaluates stream data lazily on-the-fly, reducing spatial complexity to $O(1)$ auxiliary memory.
* **Functional Paradigm:** Embedded high-order functions (`filter`) paired with `lambda` expressions shift data processing loops down to underlying C-level optimizations inside the Python interpreter.

### 3. Selection of Data Structures (Collections)
* **Lists:** Used for sequential storage of raw transaction histories where chronological tracking and rapid $O(1)$ append operations are required.
* **Dictionaries:** Utilized within `get_category_breakdown()` to map expenditures to distinct categories. This ensures amortized $O(1)$ time complexity for lookups and aggregation, maintaining a linear $O(n)$ scale for compiling financial statements.
* **Sets:** Utilized within `get_unique_categories()` to automatically discard duplicate category tags, leveraging internal hash tables for immediate uniqueness filtering.

### 4. Robustness and Testing
* **Exception Handling:** The application checks business constraints explicitly (e.g., preventing negative financial inputs by raising `ValueError`). File operations are fully wrapped in `try-except` blocks to handle system-level disruptions (`IOError`, JSON parsing errors) safely without terminating the process.
* **Automated Unit Testing:** Built-in `unittest` verification guarantees calculation validity under isolated execution environments. The `setUp` and `tearDown` methods ensure clean environmental states by managing isolated test files, eliminating data cross-contamination between test cases.

---

## Project Structure
The application follows a clean modular design with separation of concerns. All source files are located in the root repository folder:

```text
finance_tracker/
├── models.py          # Contains decorator, user profiles, and transaction class hierarchy
├── tracker.py         # Handles data storage logic, core analytics, and JSON file I/O
├── main.py            # Execution entry point simulating application life cycle
└── test_tracker.py    # Automated suite containing unit tests for core services
