# PAASWORD-strength
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

### 3. Check Password L
