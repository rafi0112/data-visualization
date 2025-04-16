# 📊 Student CGPA Data Visualization

This project presents a simple and interactive data visualization dashboard using **Streamlit** and **Matplotlib** to analyze and compare student CGPA data across semesters.

---

## 📁 Project Structure

├── students.json # Contains student data with IDs, names, and CGPAs ├── app.py # Main Streamlit application ├── README.md # Project documentation


---

## 🎯 Purpose of the Project

The goal of this project is to **visualize academic performance** of students using bar charts. It helps:

- Simplify and interpret complex student data.
- Visually compare CGPA scores across semesters.
- Highlight high and low performers.
- Enable interactive data exploration.

---

## 🧰 Tools and Technologies Used

| Tool         | Description |
|--------------|-------------|
| **Streamlit** | For creating interactive web dashboards |
| **Matplotlib** | For generating bar charts |
| **JSON** | To store and load student data |

---

## 📈 Visualization Features

- **Bar Charts:** Ideal for comparing student IDs with CGPA values.
- **Color Gradient:** Uses Plasma colormap to add visual differentiation.
- **Labeled Bars:** CGPA values are displayed on top of each bar for clarity.
- **Interactive Sidebar:** Users can choose the semester to view data for.
- **Data Table View:** Optional toggle to show raw CGPA data in tabular form.

---

## 📂 Data Format (students.json)

```json
[
  {
    "id": "S001",
    "name": "Alice",
    "semesters": {
      "1": 3.5,
      "2": 3.7,
      "3": 3.9,
      "4": 3.8
    }
  },
  ...
]
🚀 How to Run the App

git clone https://github.com/yourusername/student-cgpa-visualization.git
cd student-cgpa-visualization


Install dependencies:
pip install streamlit matplotlib

Run the app:
streamlit run app.py


📌 Example Output
Colorful bar chart showing CGPA per student for a selected semester.

Scrollable chart if number of students is large.

Table with student names, IDs, and CGPAs (optional via sidebar).

📚 Credits
Created by [Your Name]
Powered by Python 🐍, Streamlit, and Matplotlib 🎨


---

Let me know if you want to include an image preview, badges, or links to GitHub/pages.


