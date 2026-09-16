# Password Strength Checker

## Project Description

Password Strength Checker is a simple Python program that checks the strength of a password entered by the user.

The program gives a score based on five basic conditions:

* Password length
* Uppercase letter
* Lowercase letter
* Number
* Special character

It also checks whether the password is a common or simple password and provides suggestions to improve password strength.

## Aim

The main aim of this project is to understand basic password security using Python.

The program helps users identify weak passwords and understand what makes a password stronger.

## Features

* Checks whether the password has at least 8 characters.
* Checks for at least one uppercase letter.
* Checks for at least one lowercase letter.
* Checks for at least one number.
* Checks for at least one special character.
* Detects some common passwords.
* Calculates a password strength score.
* Provides suggestions when a requirement is missing.

## Technologies Used

* Python
* `re` (Regular Expression) module

## Password Scoring System

The program starts with a score of 0.

One point is added for each condition that is satisfied.

| Condition                  | Score |
| -------------------------- | ----: |
| Length ≥ 8 characters      |    +1 |
| Contains uppercase letter  |    +1 |
| Contains lowercase letter  |    +1 |
| Contains number            |    +1 |
| Contains special character |    +1 |

The maximum score is 5.

### Strength Levels

| Score | Strength    |
| ----: | ----------- |
|   0–2 | Weak        |
|     3 | Medium      |
|     4 | Strong      |
|     5 | Very Strong |

If the entered password is found in the program's list of common passwords, it is directly displayed as Very Weak.

## How the Program Works

### 1. Import Regular Expression Module

```python
import re
```

The `re` module is used to search for uppercase letters, lowercase letters, numbers, and special characters.

### 2. Take Password Input

The user enters a password:

```python
password = input("Enter your password: ")
```

### 3. Check Password Length

The program checks whether the password contains at least 8 characters.

```python
if len(password) >= 8:
```

If the condition is satisfied, the score increases by 1.

### 4. Check Uppercase Letter

The program searches for letters from A-Z.

```python
re.search(r"[A-Z]", password)
```

### 5. Check Lowercase Letter

The program searches for letters from a-z.

```python
re.search(r"[a-z]", password)
```

### 6. Check Number

The program searches for a number from 0-9.

```python
re.search(r"[0-9]", password)
```

### 7. Check Special Character

The program checks for a character that is not a letter or number.

```python
re.search(r"[^A-Za-z0-9]", password)
```

Examples include:

```text
! @ # $ % &
```

### 8. Check Common Passwords

The program contains a small list of common passwords:

```python
["password", "12345678", "qwerty", "password123", "admin"]
```

If the entered password matches one of these, the program displays:

```text
Strength: Very Weak
Suggestion: Avoid common passwords.
```

### 9. Display Suggestions

If any requirement is missing, the program displays suggestions to improve the password.

For example:

```text
Suggestions to improve your password:
- Add at least one uppercase letter (A-Z).
- Add at least one special character (!, @, #, $, etc.).
```

## Example Output

### Strong Password

```text
===== PASSWORD STRENGTH CHECKER =====
Enter your password: Hello123!

Password Strength: Very Strong

Your password meets all basic strength checks!
```

### Weak Password

```text
===== PASSWORD STRENGTH CHECKER =====
Enter your password: hello

Password Strength: Weak

Suggestions to improve your password:
- Use at least 8 characters.
- Add at least one uppercase letter (A-Z).
- Add at least one number (0-9).
- Add at least one special character (!, @, #, $, etc.).
```

### Common Password

```text
===== PASSWORD STRENGTH CHECKER =====
Enter your password: password

Strength: Very Weak
Suggestion: Avoid common passwords.
```

## How to Run the Project

### Step 1: Open Terminal

Go to the folder where the Python file is saved.

### Step 2: Run the Program

```bash
python password_checker.py
```

### Step 3: Enter Your Password

The program will check the password and display its strength and suggestions.

## Concepts Used

This project demonstrates the following Python concepts:

* Variables
* User input
* If-else conditions
* Lists
* For loops
* Regular expressions
* String methods
* Score-based decision making

## Learning Outcomes

After completing this project, you can understand:

* How to take user input in Python.
* How to use conditional statements.
* How to work with lists.
* How to use regular expressions.
* How password requirements can be checked programmatically.
* How to provide suggestions based on conditions.
* Basic concepts of password security.

## Security Note

This project is intended for educational purposes. It performs basic password-strength checks and should not be considered a complete password-security system.

Do not enter real passwords into programs or repositories that are not designed to securely handle sensitive information.

## Future Improvements

The project can be improved by adding:

* A larger common-password database.
* A password generator.
* More detailed password analysis.
* Detection of repeated characters or simple patterns.
* A graphical user interface (GUI).
* Better protection for password input.

## Author

Sneha Kumari


