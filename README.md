# 💰 Tip Calculator

A simple and beginner-friendly **Python Tip Calculator** that calculates the total bill after adding a tip and splits the final amount equally among multiple people.

## 📌 Features

- 💵 Takes the total bill amount as input
- 💯 Allows users to choose a tip percentage
- 👥 Supports splitting the bill among multiple people
- 🧮 Calculates the total bill including the tip
- 💰 Calculates each person's contribution
- 🔢 Displays amounts rounded to 2 decimal places

## 🛠️ Technologies Used

- **Python 3**
- `input()`
- `float()`
- `int()`
- Arithmetic operators
- F-strings

## 🚀 How It Works

The program follows these steps:

1. Enter the total bill amount.
2. Enter the tip percentage.
3. Enter the number of people splitting the bill.
4. The program calculates the tip amount.
5. The tip is added to the original bill.
6. The final bill is divided equally among all people.
7. The results are displayed on the screen.

## 💻 Example

```text
Welcome to the tip calculator
What is the total bill : 100
What percentage tip would you like to give? 10, 12, 15 : 10
How many people split the bill : 2

Your total bill is $110.00
Total person = 2
Every person contribut $55.00
Thanks for visiting .
```

## 📂 Project Structure

```text
Tip-Calculator/
│
├── tip_calculator.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/tip-calculator.git
```

### 2. Navigate to the project folder

```bash
cd tip-calculator
```

### 3. Run the Python program

```bash
python tip_calculator.py
```

## 🧠 Formula Used

### Tip Amount

```text
Tip Amount = Bill × (Tip Percentage / 100)
```

### Total Bill

```text
Total Bill = Bill + Tip Amount
```

### Amount Per Person

```text
Per Person = Total Bill / Number of People
```

## 📚 What I Learned

Through this project, I practiced:

- Taking user input in Python
- Converting strings into numbers
- Performing mathematical calculations
- Using variables
- Using f-strings for formatted output
- Rounding decimal values using `.2f`
- Building a small real-world Python application

## 🎯 Future Improvements

Some possible improvements for this project:

- Add input validation
- Add support for custom tip percentages
- Prevent division by zero
- Create a graphical user interface (GUI)
- Add currency selection
- Add a bill breakdown for each person

## 👨‍💻 Author

**Ritu Raj**

Data Science Enthusiast | Python & SQL | Machine Learning & AI

---

⭐ If you found this project useful, consider giving the repository a star!