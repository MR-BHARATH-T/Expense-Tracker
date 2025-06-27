# from flask import Flask, render_template, request, redirect, url_for
# import json
# from datetime import datetime
# import matplotlib.pyplot as plt
# import os


# app = Flask(__name__)
# DATA_FILE = 'expenses.json'

# # Load existing expenses
# def load_expenses():
#     try:
#         with open(DATA_FILE, 'r') as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# # Save expenses
# def save_expenses(expenses):
#     with open(DATA_FILE, 'w') as file:
#         json.dump(expenses, file, indent=4)

# # Homepage - Add expense
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         amount = float(request.form['amount'])
#         category = request.form['category']
#         date = request.form['date'] or datetime.today().strftime('%Y-%m-%d')

#         expense = {'amount': amount, 'category': category, 'date': date}
#         expenses = load_expenses()
#         expenses.append(expense)
#         save_expenses(expenses)
        
#         expense = {
#             'id': len(expenses),
#             'amount': amount,
#             'category': category,
#             'date': date
#         }


#         return redirect(url_for('index'))
    
#     return render_template('index.html')

# @app.route('/delete/<int:expense_id>')
# def delete_expense(expense_id):
#     expenses = load_expenses()
#     expenses = [e for e in expenses if e['id'] != expense_id]
#     # Reassign IDs
#     for idx, e in enumerate(expenses):
#         e['id'] = idx
#     save_expenses(expenses)
#     return redirect(url_for('expense_list'))

# @app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
# def edit_expense(expense_id):
#     expenses = load_expenses()
#     expense = next((e for e in expenses if e['id'] == expense_id), None)

#     if not expense:
#         return "Expense not found", 404

#     if request.method == 'POST':
#         expense['amount'] = float(request.form['amount'])
#         expense['category'] = request.form['category']
#         expense['date'] = request.form['date']

#         save_expenses(expenses)
#         return redirect(url_for('expense_list'))

#     return render_template('edit.html', expense=expense)


# # View summary
# @app.route('/summary')
# def summary():
#     expenses = load_expenses()
#     total = sum(e['amount'] for e in expenses)
    
#     by_category = {}
#     for e in expenses:
#         cat = e['category']
#         by_category[cat] = by_category.get(cat, 0) + e['amount']
    
#     return render_template('summary.html', total=total, by_category=by_category)

# # View all expenses
# @app.route('/expenses')
# def expense_list():
#     expenses = load_expenses()
#     return render_template('list.html', expenses=expenses)

# import matplotlib.pyplot as plt
# import os

# @app.route('/graph')
# def graph():
#     expenses = load_expenses()
#     by_category = {}
#     for e in expenses:
#         by_category[e['category']] = by_category.get(e['category'], 0) + e['amount']

#     if not by_category:
#         return "No data to plot."

#     categories = list(by_category.keys())
#     amounts = list(by_category.values())

#     plt.figure(figsize=(6, 6))
#     plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
#     plt.title('Spending by Category')

#     graph_path = os.path.join('static', 'graph.png')
#     plt.savefig(graph_path)
#     plt.close()

#     return render_template('graph.html', graph_url=graph_path)


# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for
# import json
# from datetime import datetime
# import matplotlib.pyplot as plt
# import os

# app = Flask(__name__)
# DATA_FILE = 'expenses.json'

# # Load existing expenses
# def load_expenses():
#     try:
#         with open(DATA_FILE, 'r') as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# # Save expenses
# def save_expenses(expenses):
#     with open(DATA_FILE, 'w') as file:
#         json.dump(expenses, file, indent=4)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         amount = float(request.form['amount'])
#         category = request.form['category']
#         date = request.form['date'] or datetime.today().strftime('%Y-%m-%d')

#         expenses = load_expenses()
#         expense = {
#             'id': len(expenses),
#             'amount': amount,
#             'category': category,
#             'date': date
#         }
#         expenses.append(expense)
#         save_expenses(expenses)

#         return redirect(url_for('index'))

#     return render_template('index.html')

# @app.route('/summary')
# def summary():
#     expenses = load_expenses()
#     total = sum(e['amount'] for e in expenses)
#     by_category = {}
#     for e in expenses:
#         by_category[e['category']] = by_category.get(e['category'], 0) + e['amount']

#     return render_template('summary.html', total=total, by_category=by_category)

# @app.route('/expenses')
# def expense_list():
#     expenses = load_expenses()
#     return render_template('list.html', expenses=expenses)

# @app.route('/delete/<int:expense_id>')
# def delete_expense(expense_id):
#     expenses = load_expenses()
#     expenses = [e for e in expenses if e['id'] != expense_id]
#     for idx, e in enumerate(expenses):
#         e['id'] = idx
#     save_expenses(expenses)
#     return redirect(url_for('expense_list'))

# @app.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
# def edit_expense(expense_id):
#     expenses = load_expenses()
#     expense = next((e for e in expenses if e['id'] == expense_id), None)

#     if not expense:
#         return "Expense not found", 404

#     if request.method == 'POST':
#         expense['amount'] = float(request.form['amount'])
#         expense['category'] = request.form['category']
#         expense['date'] = request.form['date']
#         save_expenses(expenses)
#         return redirect(url_for('expense_list'))

#     return render_template('edit.html', expense=expense)

# @app.route('/graph')
# def graph():
#     expenses = load_expenses()
#     by_category = {}
#     for e in expenses:
#         by_category[e['category']] = by_category.get(e['category'], 0) + e['amount']

#     if not by_category:
#         return "No data to plot."

#     categories = list(by_category.keys())
#     amounts = list(by_category.values())

#     plt.figure(figsize=(6, 6))
#     plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
#     plt.title('Spending by Category')

#     graph_path = os.path.join('static', 'graph.png')
#     plt.savefig(graph_path)
#     plt.close()

#     return render_template('graph.html', graph_url=graph_path)

# if __name__ == '__main__':
#     app.run(debug=True)






# import streamlit as st
# import json
# from datetime import datetime
# import pandas as pd
# import plotly.express as px
# import hashlib
# import os

# USER_FILE = "users.json"
# DATA_FILE = "expenses.json"

# st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered", initial_sidebar_state="expanded")

# # Custom CSS
# st.markdown("""
#     <style>
#         .sidebar .sidebar-content {
#             background-color: #f7f2e8;
#         }
#         .block-container {
#             background-color: #fef9f4;
#             padding: 2rem;
#             border-radius: 15px;
#             box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
#             transition: all 0.3s ease;
#         }
#         .block-container:hover {
#             transform: scale(1.01);
#         }
#         .css-1aumxhk:hover {
#             cursor: pointer;
#         }
#         @media (max-width: 768px) {
#             .block-container {
#                 padding: 1rem;
#             }
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Utility Functions
# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# def load_users():
#     if not os.path.exists(USER_FILE):
#         return {}
#     with open(USER_FILE, 'r', encoding='utf-8') as f:
#         return json.load(f)

# def save_users(users):
#     with open(USER_FILE, 'w', encoding='utf-8') as f:
#         json.dump(users, f, indent=4, ensure_ascii=False)

# def register_user(name, email, password):
#     users = load_users()
#     if email in users:
#         return False, "User already exists."
#     users[email] = {
#         "name": name,
#         "password": hash_password(password)
#     }
#     save_users(users)
#     return True, "Registration successful!"

# def login_user(email, password):
#     users = load_users()
#     hashed = hash_password(password)
#     if email in users and users[email]["password"] == hashed:
#         return True, users[email]["name"]
#     return False, "Invalid credentials."

# def load_all_data():
#     if not os.path.exists(DATA_FILE):
#         return {}
#     with open(DATA_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)

# def save_all_data(data):
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)

# def load_expenses(email):
#     data = load_all_data()
#     return data.get(email, [])

# def save_expenses(email, expenses):
#     data = load_all_data()
#     data[email] = expenses
#     save_all_data(data)

# def add_expense(email, amount, category, date):
#     expense = {"amount": amount, "category": category, "date": date}
#     expenses = load_expenses(email)
#     expenses.append(expense)
#     save_expenses(email, expenses)

# def delete_expense(email, index):
#     expenses = load_expenses(email)
#     if 0 <= index < len(expenses):
#         expenses.pop(index)
#         save_expenses(email, expenses)

# def edit_expense(email, index, amount, category, date):
#     expenses = load_expenses(email)
#     if 0 <= index < len(expenses):
#         expenses[index] = {"amount": amount, "category": category, "date": date}
#         save_expenses(email, expenses)

# def show_summary(email):
#     expenses = load_expenses(email)
#     total = sum(e["amount"] for e in expenses)
#     st.markdown(f"### 📊 Total Spent: ₹{total:.2f}")

#     df = pd.DataFrame(expenses)
#     if df.empty:
#         return

#     df["date"] = pd.to_datetime(df["date"])
#     df["month"] = df["date"].dt.to_period("M")
#     df["year"] = df["date"].dt.year
#     df["category"] = df["category"].str.title()

#     st.markdown("#### 💡 By Category")
#     cat_summary = df.groupby("category")["amount"].sum().reset_index()
#     for _, row in cat_summary.iterrows():
#         st.write(f"- {row['category']}: ₹{row['amount']:.2f}")

#     st.markdown("#### 🗓 Monthly Summary")
#     month_summary = df.groupby("month")["amount"].sum().reset_index()
#     for _, row in month_summary.iterrows():
#         st.write(f"- {row['month']}: ₹{row['amount']:.2f}")

#     st.markdown("#### 📅 Yearly Summary")
#     year_summary = df.groupby("year")["amount"].sum().reset_index()
#     for _, row in year_summary.iterrows():
#         st.write(f"- {row['year']}: ₹{row['amount']:.2f}")

#     if not cat_summary.empty:
#         fig = px.bar(cat_summary, x="category", y="amount", title="📊 Expenses by Category", color="category")
#         st.plotly_chart(fig)

#     st.markdown("#### 🌈 Expense Pie Chart")
#     if not cat_summary.empty:
#         fig = px.pie(cat_summary, values="amount", names="category", title="Category Share")
#         st.plotly_chart(fig)

# # Main App
# def main():
#     st.title("💸 Personal Expense Tracker")

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.email = ""
#         st.session_state.name = ""

#     if not st.session_state.logged_in:
#         tabs = st.tabs(["🔑 Login", "📝 Register"])

#         with tabs[0]:
#             st.subheader("🔐 Login")
#             email = st.text_input("Email", key="login_email")
#             password = st.text_input("Password", type="password", key="login_password")
#             if st.button("Login"):
#                 success, result = login_user(email, password)
#                 if success:
#                     st.session_state.logged_in = True
#                     st.session_state.email = email
#                     st.session_state.name = result
#                     st.success(f"Welcome, {result}!")
#                     # st.experimental_rerun()
#                     st.rerun()
#                 else:
#                     st.error(result)

#         with tabs[1]:
#             st.subheader("📝 Register")
#             name = st.text_input("Full Name", key="register_name")
#             email = st.text_input("Email", key="register_email")
#             password = st.text_input("Password", type="password", key="register_password")
#             confirm = st.text_input("Confirm Password", type="password", key="register_confirm")
#             if st.button("Register"):
#                 if password != confirm:
#                     st.error("Passwords do not match.")
#                 elif not name or not email or not password:
#                     st.error("All fields are required.")
#                 else:
#                     success, msg = register_user(name, email, password)
#                     if success:
#                         st.success(msg)
#                         st.info("Now login with your credentials.")
#                     else:
#                         st.error(msg)
#         return

#     email = st.session_state.email
#     name = st.session_state.name

#     menu = ["Add Expense", "View Expenses", "Edit/Delete", "Visual Summary"]
#     choice = st.sidebar.radio("🔍 Menu", menu)
#     st.sidebar.markdown(f"👋 Logged in as: **{name}**")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         # st.experimental_rerun()
#         st.rerun()

#     if choice == "Add Expense":
#         st.header("➕ Add a New Expense")
#         amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#         category = st.text_input("Category", placeholder="e.g., Food, Travel, etc.")
#         date = st.date_input("Date", datetime.today())
#         if st.button("Add Expense"):
#             add_expense(email, amount, category, date.strftime("%Y-%m-%d"))
#             st.success("✅ Expense added successfully!")

#     elif choice == "View Expenses":
#         st.header("📋 All Expenses")
#         expenses = load_expenses(email)
#         if not expenses:
#             st.warning("No expenses recorded.")
#         else:
#             for idx, e in enumerate(expenses):
#                 st.write(f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}")

#     elif choice == "Edit/Delete":
#         st.header("✏️ Edit or 🗑️ Delete an Expense")
#         expenses = load_expenses(email)
#         if not expenses:
#             st.warning("No expenses to modify.")
#         else:
#             options = [f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}" for idx, e in enumerate(expenses)]
#             selected = st.selectbox("Select Expense", options)
#             index = options.index(selected)
#             e = expenses[index]
#             amount = st.number_input("New Amount", value=float(e["amount"]), format="%.2f")
#             category = st.text_input("New Category", value=e["category"])
#             date = st.date_input("New Date", datetime.strptime(e["date"], "%Y-%m-%d"))

#             col1, col2 = st.columns(2)
#             if col1.button("Update"):
#                 edit_expense(email, index, amount, category, date.strftime("%Y-%m-%d"))
#                 st.success("✅ Expense updated successfully!")
#             if col2.button("Delete"):
#                 delete_expense(email, index)
#                 st.success("🗑️ Expense deleted!")

#     elif choice == "Visual Summary":
#         st.header("📈 Expense Summary")
#         show_summary(email)

# if __name__ == "__main__":
#     main()






# Expense Tracker with Firebase Auth and Google Sign-In (Simulated)

# import streamlit as st
# import json
# from datetime import datetime
# import pandas as pd
# import plotly.express as px
# import hashlib
# import os
# import pyrebase
# from firebase_config import firebase_config

# firebase = pyrebase.initialize_app(firebase_config)
# auth = firebase.auth()

# USER_FILE = "users.json"  # still used for offline name reference
# DATA_FILE = "expenses.json"

# st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered", initial_sidebar_state="expanded")

# st.markdown("""
#     <style>
#         .sidebar .sidebar-content {
#             background-color: #f7f2e8;
#         }
#         .block-container {
#             background-color: #fef9f4;
#             padding: 2rem;
#             border-radius: 15px;
#             box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
#             transition: all 0.3s ease;
#         }
#         .block-container:hover {
#             transform: scale(1.01);
#         }
#         .css-1aumxhk:hover {
#             cursor: pointer;
#         }
#         @media (max-width: 768px) {
#             .block-container {
#                 padding: 1rem;
#             }
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Expense Management Functions remain unchanged (no edits)
# def load_all_data():
#     if not os.path.exists(DATA_FILE):
#         return {}
#     with open(DATA_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)

# def save_all_data(data):
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)

# def load_expenses(email):
#     data = load_all_data()
#     return data.get(email, [])

# def save_expenses(email, expenses):
#     data = load_all_data()
#     data[email] = expenses
#     save_all_data(data)

# def add_expense(email, amount, category, date):
#     expense = {"amount": amount, "category": category, "date": date}
#     expenses = load_expenses(email)
#     expenses.append(expense)
#     save_expenses(email, expenses)

# def delete_expense(email, index):
#     expenses = load_expenses(email)
#     if 0 <= index < len(expenses):
#         expenses.pop(index)
#         save_expenses(email, expenses)

# def edit_expense(email, index, amount, category, date):
#     expenses = load_expenses(email)
#     if 0 <= index < len(expenses):
#         expenses[index] = {"amount": amount, "category": category, "date": date}
#         save_expenses(email, expenses)

# def show_summary(email):
#     expenses = load_expenses(email)
#     total = sum(e["amount"] for e in expenses)
#     st.markdown(f"### 📊 Total Spent: ₹{total:.2f}")

#     df = pd.DataFrame(expenses)
#     if df.empty:
#         return

#     df["date"] = pd.to_datetime(df["date"])
#     df["month"] = df["date"].dt.to_period("M")
#     df["year"] = df["date"].dt.year
#     df["category"] = df["category"].str.title()

#     st.markdown("#### 💡 By Category")
#     cat_summary = df.groupby("category")["amount"].sum().reset_index()
#     for _, row in cat_summary.iterrows():
#         st.write(f"- {row['category']}: ₹{row['amount']:.2f}")

#     st.markdown("#### 🗓 Monthly Summary")
#     month_summary = df.groupby("month")["amount"].sum().reset_index()
#     for _, row in month_summary.iterrows():
#         st.write(f"- {row['month']}: ₹{row['amount']:.2f}")

#     st.markdown("#### 📅 Yearly Summary")
#     year_summary = df.groupby("year")["amount"].sum().reset_index()
#     for _, row in year_summary.iterrows():
#         st.write(f"- {row['year']}: ₹{row['amount']:.2f}")

#     if not cat_summary.empty:
#         fig = px.bar(cat_summary, x="category", y="amount", title="📊 Expenses by Category", color="category")
#         st.plotly_chart(fig)

#     st.markdown("#### 🌈 Expense Pie Chart")
#     if not cat_summary.empty:
#         fig = px.pie(cat_summary, values="amount", names="category", title="Category Share")
#         st.plotly_chart(fig)

# def main():
#     st.title("💸 Personal Expense Tracker")

#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#         st.session_state.email = ""
#         st.session_state.name = ""

#     if not st.session_state.logged_in:
#         tabs = st.tabs(["🔑 Login", "📝 Register", "🔐 Forgot Password", "🔓 Google Sign-In"])

#         with tabs[0]:
#             st.subheader("🔐 Login")
#             email = st.text_input("Email", key="login_email")
#             password = st.text_input("Password", type="password", key="login_pass")
#             if st.button("Login"):
#                 try:
#                     user = auth.sign_in_with_email_and_password(email, password)
#                     st.session_state.logged_in = True
#                     st.session_state.email = email
#                     st.session_state.name = email.split("@")[0]
#                     st.success(f"Welcome, {st.session_state.name}!")
#                     st.rerun()
#                 except:
#                     st.error("Invalid credentials or Firebase error.")

#         with tabs[1]:
#             st.subheader("📝 Register")
#             email = st.text_input("Email", key="reg_email")
#             password = st.text_input("Password", type="password", key="reg_pass")
#             confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
#             if st.button("Register"):
#                 if password != confirm:
#                     st.warning("Passwords do not match.")
#                 else:
#                     try:
#                         auth.create_user_with_email_and_password(email, password)
#                         st.success("Registered successfully! Now login.")
#                     except:
#                         st.error("Registration failed. Try a different email.")

#         with tabs[2]:
#             st.subheader("🔐 Forgot Password")
#             email = st.text_input("Enter your registered email", key="forgot_email")
#             if st.button("Reset Password"):
#                 try:
#                     auth.send_password_reset_email(email)
#                     st.success("Reset email sent! Check your inbox.")
#                 except:
#                     st.error("Error sending email. Check your input.")

#         with tabs[3]:
#             st.subheader("🔓 Google Sign-In")
#             st.markdown("Google OAuth is supported via Firebase Hosting/Web only.")
#             if st.button("Simulate Google Login"):
#                 st.session_state.logged_in = True
#                 st.session_state.email = "googleuser@gmail.com"
#                 st.session_state.name = "Google User"
#                 st.success("Logged in as Google User")
#                 st.rerun()

#         return

#     # After Login
#     email = st.session_state.email
#     name = st.session_state.name

#     menu = ["Add Expense", "View Expenses", "Edit/Delete", "Visual Summary"]
#     choice = st.sidebar.radio("🔍 Menu", menu)
#     st.sidebar.markdown(f"👋 Logged in as: **{name}**")
#     if st.sidebar.button("🚪 Logout"):
#         st.session_state.logged_in = False
#         st.rerun()

#     if choice == "Add Expense":
#         st.header("➕ Add a New Expense")
#         amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#         category = st.text_input("Category", placeholder="e.g., Food, Travel, etc.")
#         date = st.date_input("Date", datetime.today())
#         if st.button("Add Expense"):
#             add_expense(email, amount, category, date.strftime("%Y-%m-%d"))
#             st.success("✅ Expense added successfully!")

#     elif choice == "View Expenses":
#         st.header("📋 All Expenses")
#         expenses = load_expenses(email)
#         if not expenses:
#             st.warning("No expenses recorded.")
#         else:
#             for idx, e in enumerate(expenses):
#                 st.write(f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}")

#     elif choice == "Edit/Delete":
#         st.header("✏️ Edit or 🗑️ Delete an Expense")
#         expenses = load_expenses(email)
#         if not expenses:
#             st.warning("No expenses to modify.")
#         else:
#             options = [f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}" for idx, e in enumerate(expenses)]
#             selected = st.selectbox("Select Expense", options)
#             index = options.index(selected)
#             e = expenses[index]
#             amount = st.number_input("New Amount", value=float(e["amount"]), format="%.2f")
#             category = st.text_input("New Category", value=e["category"])
#             date = st.date_input("New Date", datetime.strptime(e["date"], "%Y-%m-%d"))

#             col1, col2 = st.columns(2)
#             if col1.button("Update"):
#                 edit_expense(email, index, amount, category, date.strftime("%Y-%m-%d"))
#                 st.success("✅ Expense updated successfully!")
#             if col2.button("Delete"):
#                 delete_expense(email, index)
#                 st.success("🗑️ Expense deleted!")

#     elif choice == "Visual Summary":
#         st.header("📈 Expense Summary")
#         show_summary(email)

# if __name__ == "__main__":
#     main()





import streamlit as st
import json
from datetime import datetime
import pandas as pd
import plotly.express as px
import hashlib
import os
import random

USER_FILE = "users.json"
DATA_FILE = "expenses.json"

st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered", initial_sidebar_state="expanded")

# Apply Dark Theme CSS
st.markdown("""
    <style>
        body, .reportview-container, .main, .sidebar .sidebar-content {
            background-color: #121212;
            color: #e0e0e0;
        }
        .stButton>button {
            background-color: #1f1f1f;
            color: white;
            border: 1px solid #444;
        }
        .stTextInput>div>input {
            background-color: #1e1e1e;
            color: white;
        }
        .stDateInput>div>input {
            background-color: #1e1e1e;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Helper Functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)

def register_user(name, email, password):
    users = load_users()
    if email in users:
        return False, "User already exists."
    users[email] = {
        "name": name,
        "password": hash_password(password)
    }
    save_users(users)
    return True, "Registration successful!"

def login_user(email, password):
    users = load_users()
    hashed = hash_password(password)
    if email in users and users[email]["password"] == hashed:
        return True, users[email]["name"]
    return False, "Invalid credentials."

def reset_password(email, new_password):
    users = load_users()
    if email in users:
        users[email]["password"] = hash_password(new_password)
        save_users(users)
        return True
    return False

# OTP Simulation for Forgot Password
otp_store = {}
def send_fake_otp(email):
    otp = str(random.randint(100000, 999999))
    otp_store[email] = otp
    return otp

def load_all_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_all_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_expenses(email):
    data = load_all_data()
    return data.get(email, [])

def save_expenses(email, expenses):
    data = load_all_data()
    data[email] = expenses
    save_all_data(data)

def add_expense(email, amount, category, date):
    expense = {"amount": amount, "category": category, "date": date}
    expenses = load_expenses(email)
    expenses.append(expense)
    save_expenses(email, expenses)

def delete_expense(email, index):
    expenses = load_expenses(email)
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(email, expenses)

def edit_expense(email, index, amount, category, date):
    expenses = load_expenses(email)
    if 0 <= index < len(expenses):
        expenses[index] = {"amount": amount, "category": category, "date": date}
        save_expenses(email, expenses)

def show_summary(email):
    expenses = load_expenses(email)
    total = sum(e["amount"] for e in expenses)
    st.markdown(f"### 📊 Total Spent: ₹{total:.2f}")

    df = pd.DataFrame(expenses)
    if df.empty:
        return

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    df["year"] = df["date"].dt.year
    df["category"] = df["category"].str.title()

    st.markdown("#### 💡 By Category")
    cat_summary = df.groupby("category")["amount"].sum().reset_index()
    for _, row in cat_summary.iterrows():
        st.write(f"- {row['category']}: ₹{row['amount']:.2f}")

    st.markdown("#### 🗓 Monthly Summary")
    month_summary = df.groupby("month")["amount"].sum().reset_index()
    for _, row in month_summary.iterrows():
        st.write(f"- {row['month']}: ₹{row['amount']:.2f}")

    st.markdown("#### 📅 Yearly Summary")
    year_summary = df.groupby("year")["amount"].sum().reset_index()
    for _, row in year_summary.iterrows():
        st.write(f"- {row['year']}: ₹{row['amount']:.2f}")

    if not cat_summary.empty:
        fig = px.bar(cat_summary, x="category", y="amount", title="📊 Expenses by Category", color="category")
        st.plotly_chart(fig)

    st.markdown("#### 🌈 Expense Pie Chart")
    if not cat_summary.empty:
        fig = px.pie(cat_summary, values="amount", names="category", title="Category Share")
        st.plotly_chart(fig)

# Main App

def main():
    st.title("💸 Personal Expense Tracker")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.email = ""
        st.session_state.name = ""

    if not st.session_state.logged_in:
        tabs = st.tabs(["🔐 Login", "📝 Register", "🔁 Forgot Password"])

        with tabs[0]:
            st.subheader("🔐 Login")
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login"):
                success, result = login_user(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.email = email
                    st.session_state.name = result
                    st.success(f"Welcome, {result}!")
                    st.rerun()
                else:
                    st.error(result)

        with tabs[1]:
            st.subheader("📝 Register")
            name = st.text_input("Full Name", key="register_name")
            email = st.text_input("Email", key="register_email")
            password = st.text_input("Password", type="password", key="register_password")
            confirm = st.text_input("Confirm Password", type="password", key="register_confirm")
            if st.button("Register"):
                if password != confirm:
                    st.error("Passwords do not match.")
                elif not name or not email or not password:
                    st.error("All fields are required.")
                else:
                    success, msg = register_user(name, email, password)
                    if success:
                        st.success(msg)
                        st.info("Now login with your credentials.")
                    else:
                        st.error(msg)

        with tabs[2]:
            st.subheader("🔁 Forgot Password")
            email = st.text_input("Enter your registered Email", key="forgot_email")
            if st.button("Send OTP"):
                otp = send_fake_otp(email)
                st.session_state.otp_email = email
                st.session_state.otp_code = otp
                st.success(f"Simulated OTP sent: {otp}")
            if "otp_code" in st.session_state:
                entered_otp = st.text_input("Enter OTP", key="otp_input")
                new_pass = st.text_input("New Password", type="password", key="new_pass")
                if st.button("Reset Password"):
                    if entered_otp == st.session_state.otp_code:
                        reset_password(st.session_state.otp_email, new_pass)
                        st.success("Password updated successfully!")
                        del st.session_state.otp_code
                    else:
                        st.error("Incorrect OTP")
        return

    email = st.session_state.email
    name = st.session_state.name

    menu = ["Add Expense", "View Expenses", "Edit/Delete", "Visual Summary"]
    choice = st.sidebar.radio("🔍 Menu", menu)
    st.sidebar.markdown(f"👋 Logged in as: **{name}**")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    if choice == "Add Expense":
        st.header("➕ Add a New Expense")
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        category = st.text_input("Category", placeholder="e.g., Food, Travel, etc.")
        date = st.date_input("Date", datetime.today())
        if st.button("Add Expense"):
            add_expense(email, amount, category, date.strftime("%Y-%m-%d"))
            st.success("✅ Expense added successfully!")

    elif choice == "View Expenses":
        st.header("📋 All Expenses")
        expenses = load_expenses(email)
        if not expenses:
            st.warning("No expenses recorded.")
        else:
            for idx, e in enumerate(expenses):
                st.write(f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}")

    elif choice == "Edit/Delete":
        st.header("✏️ Edit or 🗑️ Delete an Expense")
        expenses = load_expenses(email)
        if not expenses:
            st.warning("No expenses to modify.")
        else:
            options = [f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}" for idx, e in enumerate(expenses)]
            selected = st.selectbox("Select Expense", options)
            index = options.index(selected)
            e = expenses[index]
            amount = st.number_input("New Amount", value=float(e["amount"]), format="%.2f")
            category = st.text_input("New Category", value=e["category"])
            date = st.date_input("New Date", datetime.strptime(e["date"], "%Y-%m-%d"))

            col1, col2 = st.columns(2)
            if col1.button("Update"):
                edit_expense(email, index, amount, category, date.strftime("%Y-%m-%d"))
                st.success("✅ Expense updated successfully!")
            if col2.button("Delete"):
                delete_expense(email, index)
                st.success("🗑️ Expense deleted!")

    elif choice == "Visual Summary":
        st.header("📈 Expense Summary")
        show_summary(email)

if __name__ == "__main__":
    main()
