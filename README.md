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

# 📊 Student CGPA Data Visualization

An interactive Streamlit dashboard to visualize student CGPA data across different semesters using colorful bar charts and a JSON data source.

---

## 📂 Data Format (`students.json`)


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
  {
    "id": "S002",
    "name": "Bob",
    "semesters": {
      "1": 3.2,
      "2": 3.4,
      "3": 3.6,
      "4": 3.5
    }
  }
]

## 🚀 Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository


git clone https://github.com/rafi0112/data-visualization.git
cd student-cgpa-visualization

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine:

### 1. Install Dependencies

Make sure Python is installed on your system. Then, install the required Python libraries:


pip install streamlit matplotlib

### ▶️ Run the Application

To launch the Streamlit app, use the following command in your terminal:


streamlit run app.py

