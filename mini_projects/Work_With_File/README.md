
# 🛒 Simple CLI Store App in Python

A simple **Command-Line Store Management System** written in Python.

This project allows users to:
- Add, edit, and remove products
- Search for products by ID or name
- View a list of all products
- Simulate buying products and updating stock
- Save and load data from a file (`database.txt`)

---

## 📂 Project Structure

```
store.py         # Main Python file (store logic)
database.txt     # Text file containing product data
```

---

## 🧪 Sample Data (`database.txt`)

```
1001,piaz,3600,40
1002,sos,15000,24
1005,keyk,48000,24
1006,hibye,49000,68
1003,chips,123500,49
```

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then open a terminal and run:

```bash
python store.py
```

Use the number-based menu to interact with the app.

---

## 📌 Features

- CLI-based menu system
- Persistent data through file read/write
- `tabulate` library for neat table display
- Basic basket system for tracking purchases

---

## 🔧 Requirements

Install the required package with pip:

```bash
pip install tabulate
```

---

## 🚀 Future Ideas (To-Do List)

- Add JSON or SQLite support for better data handling
- Improve input validation and error handling
- Refactor into Object-Oriented design
- Implement product sorting and filtering
- Save purchase history and generate invoices

---

## 💡 Author

**Sajjad** – C# Developer learning Python & AI.  
[GitHub Profile](https://github.com/SajjadSaljoghi)

---

## 📜 License

This project is open source and free to use for learning purposes.
