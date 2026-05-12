# 📊 Productivity Tracker

An interactive dashboard built with **Streamlit** to help users log and visualize their daily productivity habits.  
Track study hours, coding practice, phone usage, breaks, and sleep — and see your progress through clean charts.

---

## ✨ Features
- **Dual Modes**
  - **Example Mode**: Load sample data (`productivity.csv`) to explore the dashboard.
  - **User Mode**: Enter your own daily data, saved in a personal CSV file (`<username>_productivity.csv`).
- **Visualizations**
  - 📈 Line Chart: Study vs Coding hours over time.
  - 🍩 Donut Chart: Distribution of Study, Phone, and Coding.
  - 🥧 Pie Chart: Breaks, Phone, and Sleep balance.
- **Data Persistence**: Each user’s entries are stored in their own file, allowing dashboards to grow day by day.
- **Error Handling**: Clean conversion of inputs, defaults for blanks, and clear feedback messages.
- **Neat Layout**: Proper chart sizes, readable labels, rotated date ticks for clarity.

---

## 🛠 Tech Stack
- Python  
- Streamlit (interactive web app framework)  
- Pandas (data handling)  
- Matplotlib (visualizations)  

---

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/koramlahari2/productivity-tracker.git
cd productivity-tracker
### 2. Install dependenices
pip install -r requirements.txt
### 3. Run the APP
streamlit run tracker.py
