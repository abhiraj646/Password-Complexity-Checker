# 🔐 Password Complexity Checker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

A simple yet powerful **Python tool** that analyzes the **strength of any password** using key security criteria such as length, character variety, numbers, and special characters.  
Perfect for beginners learning Python or anyone wanting a lightweight password-strength utility.

---

## 📑 Table of Contents
- [Features](#-features)  
- [How It Works](#-how-it-works)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Example Output](#-example-output)  
- [Project Structure](#-project-structure)  
- [Contributing](#-contributing)  
- [License](#-license)

---

## 🚀 Features
✔ Checks password against **5 security rules**  
✔ Rates password: **Weak → Medium → Strong → Very Strong**  
✔ Gives improvement suggestions  
✔ Uses **regex** for accurate detection  
✔ Simple & beginner-friendly code  
✔ No external libraries required  

---

## 🧠 How It Works

The tool evaluates your password using **regular expressions**:

| Criteria | Regex Used | Purpose |
|---------|-------------|---------|
| Uppercase | `[A-Z]` | Detects capital letters |
| Lowercase | `[a-z]` | Detects small letters |
| Numbers | `[0-9]` | Detects digits |
| Special Characters | `[\W_]` | Detects symbols & underscores |
| Length Check | `len(password)` | Measures password length |

The score is calculated based on how many criteria are met → final rating is assigned.

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/abhiraj646/Password-Complexity-Checker.git
cd Password-Complexity-Checker
