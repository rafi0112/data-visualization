import streamlit as st
import json
import matplotlib.pyplot as plt
import numpy as np

# Load student data
with open("students.json") as f:
    students = json.load(f)

# Sidebar - select semester
st.sidebar.title("Select Semester")
selected_semester = st.sidebar.selectbox("Semester", ["1", "2", "3", "4"])

# Filter CGPA data for selected semester
ids = [student["id"] for student in students]
names = [student["name"] for student in students]
cgpas = [student["semesters"][selected_semester] for student in students]

# Gradient color
colors = plt.cm.plasma(np.linspace(0.3, 1, len(cgpas)))

# Plotting
fig, ax = plt.subplots(figsize=(18, 8))
bars = ax.bar(ids, cgpas, color=colors)

# Add labels
for bar, cgpa in zip(bars, cgpas):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03, f"{cgpa:.2f}",
            ha='center', va='bottom', fontsize=9)

# Chart settings
ax.set_title(f"CGPA out of 4.0 - Semester {selected_semester}", fontsize=18)
ax.set_xlabel("Student ID")
ax.set_ylabel("CGPA")
ax.set_xticks(ids)
ax.set_ylim(0, 4.2)
ax.grid(axis='y', linestyle='--', alpha=0.5)

st.pyplot(fig)

# Optional: Display raw data
if st.sidebar.checkbox("Show data table"):
    table_data = [{"ID": s["id"], "Name": s["name"], "CGPA": s["semesters"][selected_semester]} for s in students]
    st.subheader("CGPA Data")
    st.dataframe(table_data)
