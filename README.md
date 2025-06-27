# Expense-Tracker

# 💸 Personal Expense Tracker

A modern, web-based expense tracker built with [Streamlit](https://streamlit.io/). Easily track your daily expenses, view visual summaries, and manage your spending with user-friendly charts and dashboards.

---

## 🚀 Features

- 🔐 **User Authentication**  
  Register, login, and securely manage your account using email and password.

- 🔁 **Forgot Password Flow**  
  Simulated OTP-based password recovery (no email service needed).

- 🌑 **Dark Mode UI**  
  Clean and responsive interface designed for dark mode lovers.

- ➕ **Add Expenses**  
  Quickly add expenses with categories and dates.

- 📋 **View / Edit / Delete**  
  Easily view, update, or remove individual entries.

- 📈 **Visual Dashboard**  
  Get summaries by category, month, and year with bar and pie charts.

- 💾 **Data Storage**  
  All user and expense data is stored in JSON files (`users.json` and `expenses.json`).

---

## 📸 Demo

![Screenshot](assets/demo.png) <!-- Optional: Include a screenshot in your repo -->

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Plotly**
- **Pandas**

---

## 📂 Project Structure
📦 expense_tracker/
│
├── Expense-Tracker.py # Main app script
├── users.json # User credentials (hashed)
├── expenses.json # All user expense data
└── README.md

---

## ⚙️ How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/Expense-Tracker.git
   cd Expense-Tracker

2. **Install dependencies:**

bash:
pip install streamlit pandas plotly

**3. Run the app:**

bash:
streamlit run Expense-Tracker.py

**🔒 Security Notes:**

Passwords are hashed using SHA-256.

Forgot password flow is simulated using OTP-style verification (no real email service).

For production, consider using a secure backend and encrypted storage.

**📝 License:**
This project is open-source and available under the MIT License.

**💡 Author:**
Designed by Bharath Thimmapppa
