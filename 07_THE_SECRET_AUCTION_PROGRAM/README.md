# 🔨 Blind Auction — Python

A simple **Blind Auction program** built using Python.

The program allows multiple bidders to secretly enter their names and bid amounts. After all bidders have finished, the program automatically determines the **highest bidder and winning bid**.

This project was created to practice **Python dictionaries, functions, loops, input validation, and basic problem-solving**.

---

## 📌 About the Project

A blind auction is an auction where participants enter their bids without seeing the bids of other participants.

This project simulates a blind auction using a Python dictionary.

Each bidder's name is stored as a **key**, and their bid amount is stored as the corresponding **value**.

Example:

```text
Omkar  → $500
Rahul  → $750
Amit   → $600
```

The program compares all the bids and determines:

```text
The winner is Rahul with a bid of 750
```

---

## ✨ Features

* 🔨 Supports multiple bidders
* 💰 Accepts individual bid amounts
* 🔐 Keeps bids hidden between bidders
* 🏆 Automatically finds the highest bidder
* 🔄 Allows multiple rounds of bidding
* 🧹 Clears the terminal between bidders
* 🚫 Prevents empty bidder names
* 🚫 Prevents duplicate bidder names
* ⚠️ Handles non-numeric bids
* ⚠️ Prevents negative bids
* ⚠️ Validates `yes` / `no` input
* 💻 Simple command-line interface

---

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Functions
* `while` loops
* `for` loops
* Conditional statements
* `try-except`
* User input
* String methods
* `os` module

---

## 📂 Project Structure

```text
Blind-Auction/
│
├── main.py
├── Art.py
└── README.md
```

### Files

**`main.py`**

* Contains the complete auction logic
* Collects bidder names and bids
* Validates user input
* Stores bids in a dictionary
* Finds the highest bidder

**`Art.py`**

* Contains the ASCII logo displayed by the program

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Blind-Auction
```

### 3. Run the program

```bash
python main.py
```

---

## 🎮 How to Use

### Step 1 — Enter your name

```text
What is your name?: Omkar
```

The program does not allow an empty name.

```text
What is your name?:
Name cannot be empty. Please enter your name.
```

---

### Step 2 — Enter your bid

```text
What is your bid?: 500
```

The program only accepts valid numbers.

For example:

```text
What is your bid?: abc
Invalid bid! Please enter a number.
```

Negative bids are also rejected:

```text
What is your bid?: -500
Bid cannot be negative. Please enter a valid bid.
```

---

### Step 3 — Check for more bidders

The program asks:

```text
Are there any other bidders? Type 'yes' or 'no'.
```

If the answer is `yes`, the terminal is cleared and the next bidder can enter their bid.

If the answer is `no`, the program calculates the winner.

Invalid answers are rejected:

```text
Invalid input! Please type 'yes' or 'no'.
```

---

## 🚫 Duplicate Bidder Validation

A bidder cannot enter another bid using the same name.

For example:

```text
What is your name?: Omkar
What is your bid?: 500

What is your name?: Omkar
This bidder has already placed a bid.
```

The program then asks for another bidder name.

---

## 🧠 How It Works

The program stores all bids inside a dictionary:

```python
bids = {}
```

When a bidder enters their name and bid:

```python
bids[name] = price
```

The dictionary may look like:

```python
{
    "Omkar": 500,
    "Rahul": 750,
    "Amit": 600
}
```

The `find_highest_bidder()` function then checks every bidder:

```python
for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
```

Whenever a higher bid is found, the program updates:

* `highest_bid`
* `winner`

After all bidders have been checked, the winner is displayed.

---

## 🔄 Program Flow

```text
                Start
                  │
                  ▼
             Enter Name
                  │
          ┌───────┴────────┐
          │                │
      Empty Name?          │
          │                │
         Yes               No
          │                │
          ▼                ▼
      Ask Again        Check Duplicate
                           │
                    ┌──────┴──────┐
                    │             │
                  Exists        New Name
                    │             │
                    ▼             ▼
                Ask Again     Enter Bid
                                  │
                           ┌──────┴──────┐
                           │             │
                       Invalid        Valid
                           │             │
                           ▼             ▼
                       Ask Again    Store Bid
                                         │
                                         ▼
                                  More Bidders?
                                    │       │
                                   Yes      No
                                    │       │
                                    ▼       ▼
                              Clear Screen  Find
                              & Continue   Winner
                                            │
                                            ▼
                                          End
```

---

## 📚 Concepts Learned

This project helped me practice:

* Python dictionaries
* Dictionary keys and values
* Functions
* Function parameters
* `while` loops
* `for` loops
* `if-elif-else`
* Comparison operators
* `try-except`
* User input
* String methods
* Input validation
* Duplicate checking
* Importing Python modules
* Using the `os` module
* Finding the highest value manually

---

## 🎯 Input Validation

The project handles several common user-input cases:

| Input Case           | Handling           |
| -------------------- | ------------------ |
| Empty name           | ❌ Rejected         |
| Duplicate name       | ❌ Rejected         |
| Non-numeric bid      | ❌ Rejected         |
| Negative bid         | ❌ Rejected         |
| `yes`                | ✅ Continue bidding |
| `no`                 | ✅ Finish auction   |
| Invalid yes/no input | ❌ Asks again       |

---

## 📸 Sample Output

```text
What is your name?: Omkar
What is your bid?: 500

Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?: Rahul
What is your bid?: 750

Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?: Amit
What is your bid?: 600

Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Rahul with a bid of 750
```

---

## 🎯 Future Improvements

Possible improvements for future versions:

* [ ] Support decimal bid amounts
* [ ] Add a graphical user interface
* [ ] Store auction results in a file
* [ ] Support multiple auction items
* [ ] Add auction history
* [ ] Add automated tests

---

## 👨‍💻 Author

**Omkar Narlawar**

This project was created as part of my journey of learning **Python programming, problem-solving, and data structures**.

---

⭐ If you found this project interesting, consider giving the repository a star!
