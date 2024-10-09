# Bank App

This is a simple Python-based banking application that allows users to check their balance, deposit money, and withdraw money. The application operates through a text-based interface and demonstrates basic programming logic.

## Features

- **Show Balance**: Displays the current balance.
- **Deposit**: Allows the user to deposit an amount to their balance.
- **Withdraw**: Allows the user to withdraw an amount from their balance, checking for sufficient funds.
- **Exit**: Exits the application.

## Prerequisites

- Python 3.x installed on your system.

## How to Run

1. Clone or download the repository.
2. Navigate to the directory where the `bank_app.py` file is located.
3. Run the app using the command:
    ```bash
    python bank_app.py
    ```
4. Follow the instructions displayed on the screen to interact with the application.

## Usage

The application displays a menu with the following options:


- **1. Show Balance**: Displays the current balance in the account.
- **2. Deposit**: Prompts the user to enter an amount to deposit. If the amount is valid, it is added to the balance.
- **3. Withdraw**: Prompts the user to enter an amount to withdraw. If the amount is valid and sufficient, it is deducted from the balance.
- **4. Exit**: Exits the application.

## Code Structure

- `show_balance()`: Displays the current balance.
- `deposit()`: Takes user input for the deposit amount and returns the amount if valid.
- `with_Draw()`: Takes user input for the withdrawal amount and returns the amount if it meets the conditions (not negative and less than or equal to balance).
- The application uses a `while` loop to keep the application running until the user decides to exit.

## Error Handling

- Ensures that the deposit amount is not negative.
- Checks that the withdrawal amount is not negative and does not exceed the available balance.
- Handles invalid menu choices and prompts the user to enter a valid option.

## Improvements

- Add more features such as account history, transfer between accounts, or multi-user functionality.
- Implement a GUI version of the app for a better user experience.

## License

This project is open-source and free to use.
