import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

st.title("📊 Personal Productivity Tracker")

# --- Example Mode ---
if st.button("Check Example"):
    try:
        df = pd.read_csv("productivity.csv", parse_dates=["Date"], dayfirst=True)
        st.subheader("📋 Example Data")
        st.dataframe(df)

        # Pie chart: Breaks vs Phone vs Sleep   
        st.subheader("🥧 Pie Chart: Breaks, Phone & Sleep")
        fig3, ax3 = plt.subplots(figsize=(4,4))
        sizes2 = [df["Breaks"].sum(), df["Phone_Screen_Time"].sum(), df["Sleep_Hours"].sum()]
        labels2 = ["Breaks", "Phone", "Sleep"]
        ax3.pie(sizes2, labels=labels2, autopct="%1.1f%%", startangle=90)
        ax3.set_title("Total Distribution", fontsize=11)
        st.pyplot(fig3)


        # Line chart: Study & Coding
        st.subheader("📈 Line Chart: Study & Coding Hours")
        fig1, ax1 = plt.subplots(figsize=(6,4))
        ax1.plot(df["Date"], df["Study_Hours"], marker="o", label="Study Hours", color="green")
        ax1.plot(df["Date"], df["Coding_Hours"], marker="o", label="Coding Hours", color="blue")
        ax1.set_xlabel("Date", fontsize=10)
        ax1.set_ylabel("Hours", fontsize=10)
        ax1.set_title("Study vs Coding Over Time", fontsize=12)
        ax1.legend(fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.yticks(fontsize=8)
        st.pyplot(fig1)

        # Donut chart: Study vs Phone vs Coding
        st.subheader("🍩 Donut Chart: Study vs Phone vs Coding")
        fig2, ax2 = plt.subplots(figsize=(4,4))
        sizes = [df["Study_Hours"].sum(), df["Phone_Screen_Time"].sum(), df["Coding_Hours"].sum()]
        labels = ["Study", "Phone", "Coding"]
        ax2.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
                wedgeprops=dict(width=0.4))
        ax2.set_title("Total Distribution", fontsize=11)
        st.pyplot(fig2)

        # Pie chart: Breaks vs Phone vs Sleep
        
    except FileNotFoundError:
        st.error("⚠️ Example file 'productivity.csv' not found.")

# --- User Mode ---

st.subheader("👤 Enter Your Daily Data")

username = st.text_input("Enter your name")
date = st.date_input("Select Date")

study_hours = st.text_input("Study Hours (hrs)")
coding_hours = st.text_input("Coding Hours (hrs)")
phone_time = st.text_input("Phone Screen Time (hrs)")
breaks = st.text_input("Breaks (hrs)")
sleep = st.text_input("Sleep Hours (hrs)")

if st.button("Generate My Dashboard"):
    try:
        # Convert inputs safely
        new_row = {
            "Date": str(date),  # ✅ convert date to string
            "Study_Hours": float(study_hours.strip()) if study_hours else 0.0,
            "Coding_Hours": float(coding_hours.strip()) if coding_hours else 0.0,
            "Phone_Screen_Time": float(phone_time.strip()) if phone_time else 0.0,
            "Breaks": float(breaks.strip()) if breaks else 0.0,
            "Sleep_Hours": float(sleep.strip()) if sleep else 0.0
        }

        filename = f"{username}_productivity.csv"

        if os.path.exists(filename):
            df = pd.read_csv(filename, parse_dates=["Date"])
        else:
            df = pd.DataFrame(columns=["Date","Study_Hours","Coding_Hours","Phone_Screen_Time","Breaks","Sleep_Hours"])

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(filename, index=False)

        st.success(f"✅ Data saved to {filename}")

        st.subheader("📋 Your Daily Records")
        st.dataframe(df)

        # Line chart
        st.subheader("📈 Line Chart: Study & Coding Hours")
        fig1, ax1 = plt.subplots(figsize=(6,4))
        ax1.plot(df["Date"], df["Study_Hours"], marker="o", label="Study Hours", color="green")
        ax1.plot(df["Date"], df["Coding_Hours"], marker="o", label="Coding Hours", color="blue")
        ax1.set_xlabel("Date", fontsize=10)
        ax1.set_ylabel("Hours", fontsize=10)
        ax1.set_title("Study vs Coding Over Time", fontsize=12)
        ax1.legend(fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.yticks(fontsize=8)
        st.pyplot(fig1)

        # Donut chart
        st.subheader("🍩 Donut Chart: Study vs Phone vs Coding")
        fig2, ax2 = plt.subplots(figsize=(4,4))
        sizes = [df["Study_Hours"].sum(), df["Phone_Screen_Time"].sum(), df["Coding_Hours"].sum()]
        labels = ["Study", "Phone", "Coding"]
        ax2.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
                wedgeprops=dict(width=0.4))
        ax2.set_title("Total Distribution", fontsize=11)
        st.pyplot(fig2)

        # Pie chart
        st.subheader("🥧 Pie Chart: Breaks, Phone & Sleep")
        fig3, ax3 = plt.subplots(figsize=(4,4))
        sizes2 = [df["Breaks"].sum(), df["Phone_Screen_Time"].sum(), df["Sleep_Hours"].sum()]
        labels2 = ["Breaks", "Phone", "Sleep"]
        ax3.pie(sizes2, labels=labels2, autopct="%1.1f%%", startangle=90)
        ax3.set_title("Total Distribution", fontsize=11)
        st.pyplot(fig3)

    except ValueError:
        st.error("⚠️ Please enter valid numeric values.")
