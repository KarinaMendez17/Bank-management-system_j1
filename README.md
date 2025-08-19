# 🏦 Bank Management System Simulator

## Overview
This is a **Bank Management System Simulator** written in Python.  
It emulates the core operations of a banking system, allowing users to manage clients, accounts, loans, and transactions in a realistic environment.  

---

## Features

### Client Management
- Register and validate clients with personal info.
- Verify ID numbers and email addresses.
- Personalized greetings based on gender.

### Account Management
- **Savings Account**: Deposit, withdraw, transfer funds.
- **Checking Account**: Deposit, withdraw, transfer funds.
- Delete accounts with proper handling of remaining balances.

### Loan Management
- Supports multiple types of loans:
  - Credit Card
  - Personal Loan
  - Mortgage
  - Vehicle Loan
- Withdraw funds from loans to debit accounts or cash.
- Make payments (minimum, total, partial).

### Transactions
- Deposit to own accounts or to other clients’ accounts.
- Withdraw from accounts with limits and validations.
- Transfer funds between debit accounts and loans.
- Track balances in a structured JSON database.

### Data Handling
- Persistent storage using JSON files (`clients.json`).
- Automatic updates of balances, debts, and records.
- Robust error handling and input validation.

---

## Quick Start
1. **Clone the repository**
    ```bash
git clone https://github.com/yourusername/bank-management-simulator.git
cd bank-management-simulator

2. **Run the main program**
python main.py

## Interact with the system

1. Enter your client ID.
2. Choose from the options:
   - Manage accounts (deposit, withdraw, terminate)
   - Handle loans and credits
   - Make payments
3. Follow on-screen prompts for transactions.

## Validations

- ID and account number length checks.
- Email format verification.
- Min/Max limits for deposits and withdrawals.
- Ensures sufficient funds before processing.

## Project Structure

```text
bank-management-simulator/
│
├─ data/
│ └─ clients.json # Client & account database
│
├─ modules/
│ └─ utilities.py # Helper functions (validation, greetings)
│
├─ deposit.py # Deposit functionality
├─ withdrawal.py # Withdrawals functionality
├─ payments.py # Payment functionality
├─ terminate_account.py # Account termination functionality
└─ main.py # Entry point
```
## Notes

- This is a simulation for educational purposes.
- All data is stored locally in JSON files.
- Not connected to any real banking system.

## Author
Méndez Domínguez Dulce Karina.
