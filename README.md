# Password Strength Checker

*A simple, beginner-friendly Python tool to check how strong your password is* 💡

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square)
![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)

---

## Overview

Ever wondered if your password is strong enough?
This tool gives you a quick answer by analyzing your password based on some basic but important rules.

It's built using just Python’s built-in libraries—no extra installations needed.
It gives your password a strength rating so you can decide whether to keep it or strengthen it.

---

## What It Does

The checker looks for:

* ✅ Minimum length (at least 8 characters)
* 🔠 Mix of uppercase and lowercase letters
* 🔢 Numbers
* 🔣 Special characters like `@`, `!`, `#`, etc.

Once it checks all that, it gives your password a rating:
**WEAK**, **MODERATE**, or **STRONG**.

And for added privacy, it hides your password input using Python’s `getpass` module—so no one sees what you're typing!

---

## How to Use It

### 1. Clone this repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/irfanshakeel1094/password-checker.git
cd password-checker
```

### 2. Run the tool

```bash
python password_checker.py
```

Follow the prompt and enter a password to check its strength!

---

## License

This project is open-source and available under the [MIT License](LICENSE).
Feel free to use it, improve it, or build on top of it!

---
