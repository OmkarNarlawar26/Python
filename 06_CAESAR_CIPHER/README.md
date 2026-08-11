# 🔐 Caesar Cipher — Python

A simple **Caesar Cipher encryption and decryption program** built using Python.

This project allows users to enter a message, choose whether to **encode or decode** it, and specify a shift number. The program then applies the Caesar Cipher algorithm to transform the message.

---

## 📌 What is Caesar Cipher?

The **Caesar Cipher** is one of the simplest encryption techniques.

It works by shifting each letter of the alphabet by a fixed number of positions.

For example, with a shift of **3**:

```text
Original:  hello
Shift:     3
Encoded:   khoor
```

To decrypt the message, the same shift is applied in the opposite direction:

```text
Encoded:   khoor
Shift:     3
Decoded:   hello
```

---

## ✨ Features

* 🔐 Encrypt messages using Caesar Cipher
* 🔓 Decrypt encrypted messages
* 🔄 Supports different shift values
* 🔁 Allows repeated encryption/decryption
* 📝 Preserves spaces and special characters
* 💻 Simple command-line interface
* 🧩 Uses Python functions and loops

---

## 🛠️ Technologies Used

* **Python 3**
* Python Functions
* `while` Loop
* `for` Loop
* Lists
* Strings
* Conditional Statements
* User Input

---

## 📂 Project Structure

```text
Caesar-Cipher/
│
├── main.py
├── Art.py
└── README.md
```

### Files

**`main.py`**

* Contains the main Caesar Cipher logic
* Handles user input
* Performs encryption and decryption

**`Art.py`**

* Contains the ASCII logo displayed when the program starts

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Caesar-Cipher
```

### 3. Run the program

```bash
python main.py
```

---

## 🎮 How to Use

When the program starts, choose whether you want to encode or decode a message.

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
```

Enter your message:

```text
Type your message:
hello
```

Enter the shift number:

```text
Type the shift number:
3
```

The program will produce:

```text
Here is the encoded result: khoor
```

For decoding:

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
decode

Type your message:
khoor

Type the shift number:
3

Here is the decoded result: hello
```

---

## 🧠 How It Works

The program stores the alphabet in a list:

```python
alphabet = ['a', 'b', 'c', ..., 'z']
```

For every character in the user's message, the program:

1. Checks whether the character exists in the alphabet.
2. Finds its current position.
3. Adds the specified shift value.
4. Uses modulo to handle shifts beyond `z`.
5. Adds the shifted character to the result.
6. For decoding, the shift is reversed.

The important part of the algorithm is:

```python
shifted_position = alphabet.index(letter) + shift_amount
shifted_position %= len(alphabet)
```

The modulo operation allows the alphabet to wrap around.

For example:

```text
z + 3 → c
```

---

## 🔄 Example

### Encoding

```text
Message:   python
Shift:     2

Result:    ravjqp
```

### Decoding

```text
Message:   ravjqp
Shift:     2

Result:    python
```

---

## 📚 Concepts Learned

This project helped me practice:

* Python functions
* Function parameters
* `if-elif-else`
* `for` loops
* `while` loops
* Lists
* Strings
* `.lower()`
* `.index()`
* Modulo operator `%`
* User input
* Python modules
* Basic encryption concepts

---

## 🎯 Future Improvements

Possible improvements for future versions:

* [ ] Support uppercase letters
* [ ] Add better input validation
* [ ] Handle invalid shift values
* [ ] Add a graphical user interface
* [ ] Allow custom alphabets
* [ ] Improve the command-line interface
* [ ] Add automated tests

---

## 📸 Sample Output

```text
     ______
    / _____)
   | /  ___
   | | (___
   | \____/
    \______

Type 'encode' to encrypt, type 'decode' to decrypt:
> encode

Type your message:
> hello world

Type the shift number:
> 3

Here is the encoded result: khoor zruog
```

---

## 👨‍💻 Author

**Omkar Narlawar**

This project was created as part of my journey of learning **Python programming and problem-solving**.

---

⭐ If you found this project interesting, consider giving the repository a star!
