# import streamlit as st
# import json
# from datetime import datetime
# from collections import defaultdict
# import matplotlib.pyplot as plt

# FILENAME = "expenses.json"

# def load_expenses():
#     try:
#         with open(FILENAME, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# def save_expenses(expenses):
#     with open(FILENAME, "w", encoding="utf-8") as f:
#         json.dump(expenses, f, indent=4, ensure_ascii=False)

# def add_expense(amount, category, date):
#     expense = {"amount": amount, "category": category, "date": date}
#     expenses = load_expenses()
#     expenses.append(expense)
#     save_expenses(expenses)

# def delete_expense(index):
#     expenses = load_expenses()
#     if 0 <= index < len(expenses):
#         expenses.pop(index)
#         save_expenses(expenses)

# def edit_expense(index, amount, category, date):
#     expenses = load_expenses()
#     if 0 <= index < len(expenses):
#         expenses[index] = {"amount": amount, "category": category, "date": date}
#         save_expenses(expenses)

# def show_summary(expenses):
#     total = sum(e["amount"] for e in expenses)
#     st.markdown(f"### 📊 Total Spent: ₹{total:.2f}")

#     categories = defaultdict(float)
#     for e in expenses:
#         categories[e["category"].title()] += e["amount"]
#     st.markdown("#### 💡 By Category")
#     for cat, amt in sorted(categories.items()):
#         st.write(f"- {cat}: ₹{amt:.2f}")

#     dates = defaultdict(float)
#     for e in expenses:
#         dates[e["date"]] += e["amount"]
#     st.markdown("#### 📅 Daily Totals")
#     for date, amt in sorted(dates.items()):
#         st.write(f"- {date}: ₹{amt:.2f}")

#     months = defaultdict(float)
#     for e in expenses:
#         month = e["date"][:7]
#         months[month] += e["amount"]
#     st.markdown("#### 🗓 Monthly Totals")
#     for month, amt in sorted(months.items()):
#         st.write(f"- {month}: ₹{amt:.2f}")

# def plot_pie_chart(expenses):
#     categories = defaultdict(float)
#     for e in expenses:
#         categories[e["category"].title()] += e["amount"]
#     labels = list(categories.keys())
#     values = list(categories.values())

#     if values:
#         fig, ax = plt.subplots()
#         ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
#         ax.axis("equal")
#         st.pyplot(fig)
#     else:
#         st.info("No data to display in pie chart.")

# def main():
#     st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered")
#     st.title("💸 Personal Expense Tracker")

#     menu = ["➕ Add Expense", "📋 View Expenses", "✏️ Edit/Delete", "📈 Visual Summary"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     if choice == "➕ Add Expense":
#         st.header("➕ Add a New Expense")
#         amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#         category = st.text_input("Category (e.g., Food, Travel, etc.)")
#         date = st.date_input("Date", datetime.today())
#         if st.button("Add Expense"):
#             add_expense(amount, category, date.strftime("%Y-%m-%d"))
#             st.success("✅ Expense added successfully!")

#     elif choice == "📋 View Expenses":
#         st.header("📋 All Expenses")
#         expenses = load_expenses()
#         if not expenses:
#             st.warning("No expenses recorded.")
#         else:
#             for idx, e in enumerate(expenses):
#                 st.write(f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}")

#     elif choice == "✏️ Edit/Delete":
#         st.header("✏️ Edit or 🗑️ Delete an Expense")
#         expenses = load_expenses()
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
#                 edit_expense(index, amount, category, date.strftime("%Y-%m-%d"))
#                 st.success("✅ Expense updated successfully!")
#             if col2.button("Delete"):
#                 delete_expense(index)
#                 st.success("🗑️ Expense deleted!")

#     elif choice == "📈 Visual Summary":
#         st.header("📈 Expense Summary")
#         expenses = load_expenses()
#         if not expenses:
#             st.warning("No expenses recorded yet.")
#         else:
#             show_summary(expenses)
#             st.subheader("📊 Expense Pie Chart")
#             plot_pie_chart(expenses)

# if __name__ == "__main__":
#     main()



# import streamlit as st
# import json
# from datetime import datetime
# from collections import defaultdict
# import matplotlib.pyplot as plt
# import plotly.express as px

# FILENAME = "expenses.json"

# st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered")

# # Apply custom CSS for styling and hover effect
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
#     </style>
# """, unsafe_allow_html=True)

# def load_expenses():
#     try:
#         with open(FILENAME, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# def save_expenses(expenses):
#     with open(FILENAME, "w", encoding="utf-8") as f:
#         json.dump(expenses, f, indent=4, ensure_ascii=False)

# def add_expense(amount, category, date):
#     expense = {"amount": amount, "category": category, "date": date}
#     expenses = load_expenses()
#     expenses.append(expense)
#     save_expenses(expenses)

# def delete_expense(index):
#     expenses = load_expenses()
#     if 0 <= index < len(expenses):
#         expenses.pop(index)
#         save_expenses(expenses)

# def edit_expense(index, amount, category, date):
#     expenses = load_expenses()
#     if 0 <= index < len(expenses):
#         expenses[index] = {"amount": amount, "category": category, "date": date}
#         save_expenses(expenses)

# def show_summary(expenses):
#     total = sum(e["amount"] for e in expenses)
#     st.markdown(f"### 📊 Total Spent: ₹{total:.2f}")

#     categories = defaultdict(float)
#     for e in expenses:
#         categories[e["category"].title()] += e["amount"]
#     st.markdown("#### 💡 By Category")
#     for cat, amt in sorted(categories.items()):
#         st.write(f"- {cat}: ₹{amt:.2f}")

#     # Plot bar chart
#     if categories:
#         df = {"Category": list(categories.keys()), "Amount": list(categories.values())}
#         fig = px.bar(df, x="Category", y="Amount", title="📊 Expenses by Category", color="Category")
#         st.plotly_chart(fig)

#     # Pie chart
#     st.markdown("#### 🌈 Expense Pie Chart")
#     if categories:
#         fig = px.pie(values=list(categories.values()), names=list(categories.keys()), title="Category Share")
#         st.plotly_chart(fig)

# def main():
#     st.title("💸 Personal Expense Tracker")

#     menu = ["Add Expense", "View Expenses", "Edit/Delete", "Visual Summary"]
#     choice = st.sidebar.radio("\U0001F50D Menu", menu)

#     if choice == "Add Expense":
#         st.header("➕ Add a New Expense")
#         amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#         category = st.text_input("Category (e.g., Food, Travel, etc.)")
#         date = st.date_input("Date", datetime.today())
#         if st.button("Add Expense"):
#             add_expense(amount, category, date.strftime("%Y-%m-%d"))
#             st.success("✅ Expense added successfully!")

#     elif choice == "View Expenses":
#         st.header("📋 All Expenses")
#         expenses = load_expenses()
#         if not expenses:
#             st.warning("No expenses recorded.")
#         else:
#             for idx, e in enumerate(expenses):
#                 st.write(f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}")

#     elif choice == "Edit/Delete":
#         st.header("✏️ Edit or 🗑️ Delete an Expense")
#         expenses = load_expenses()
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
#                 edit_expense(index, amount, category, date.strftime("%Y-%m-%d"))
#                 st.success("✅ Expense updated successfully!")
#             if col2.button("Delete"):
#                 delete_expense(index)
#                 st.success("🗑️ Expense deleted!")

#     elif choice == "Visual Summary":
#         st.header("📈 Expense Summary")
#         expenses = load_expenses()
#         if not expenses:
#             st.warning("No expenses recorded yet.")
#         else:
#             show_summary(expenses)

# if __name__ == "__main__":
#     main()









import streamlit as st
import json
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

FILENAME = "expenses.json"

st.set_page_config(page_title="💸 Personal Expense Tracker", layout="centered", initial_sidebar_state="expanded")

# Apply custom CSS for responsive styling and hover effect
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f7f2e8;
        }
        .block-container {
            background-color: #fef9f4;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .block-container:hover {
            transform: scale(1.01);
        }
        .css-1aumxhk:hover {
            cursor: pointer;
        }
        @media (max-width: 768px) {
            .block-container {
                padding: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

def load_expenses():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)

def add_expense(amount, category, date):
    expense = {"amount": amount, "category": category, "date": date}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)

def edit_expense(index, amount, category, date):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses[index] = {"amount": amount, "category": category, "date": date}
        save_expenses(expenses)

def show_summary(expenses):
    total = sum(e["amount"] for e in expenses)
    st.markdown(f"### 📊 Total Spent: ₹{total:.2f}")

    df = pd.DataFrame(expenses)
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

    # Bar Chart
    if not cat_summary.empty:
        fig = px.bar(cat_summary, x="category", y="amount", title="📊 Expenses by Category", color="category")
        st.plotly_chart(fig)

    # Pie Chart
    st.markdown("#### 🌈 Expense Pie Chart")
    if not cat_summary.empty:
        fig = px.pie(cat_summary, values="amount", names="category", title="Category Share")
        st.plotly_chart(fig)

def main():
    st.title("💸 Personal Expense Tracker")

    menu = ["Add Expense", "View Expenses", "Edit/Delete", "Visual Summary"]
    choice = st.sidebar.radio("🔍 Menu", menu)

    if choice == "Add Expense":
        st.header("➕ Add a New Expense")
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        category = st.text_input("Category", placeholder="e.g., Food, Travel, etc.")
        date = st.date_input("Date", datetime.today())
        if st.button("Add Expense"):
            add_expense(amount, category, date.strftime("%Y-%m-%d"))
            st.success("✅ Expense added successfully!")

    elif choice == "View Expenses":
        st.header("📋 All Expenses")
        expenses = load_expenses()
        if not expenses:
            st.warning("No expenses recorded.")
        else:
            for idx, e in enumerate(expenses):
                st.write(f"{idx+1}. ₹{e['amount']} | {e['category']} | {e['date']}")

    elif choice == "Edit/Delete":
        st.header("✏️ Edit or 🗑️ Delete an Expense")
        expenses = load_expenses()
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
                edit_expense(index, amount, category, date.strftime("%Y-%m-%d"))
                st.success("✅ Expense updated successfully!")
            if col2.button("Delete"):
                delete_expense(index)
                st.success("🗑️ Expense deleted!")

    elif choice == "Visual Summary":
        st.header("📈 Expense Summary")
        expenses = load_expenses()
        if not expenses:
            st.warning("No expenses recorded yet.")
        else:
            show_summary(expenses)

if __name__ == "__main__":
    main()
