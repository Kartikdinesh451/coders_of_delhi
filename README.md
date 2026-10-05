# 👥 Coders of Delhi — Social Network Recommendation & Data Cleaning

A Python-based mini social-network analytics project that works with JSON data to demonstrate **data loading, data cleaning, relationship analysis, and rule-based recommendations**.

> **Portfolio focus:** Python • JSON • Data Cleaning • Recommendation Logic • Data Analysis

---

## 🎯 Project Overview

This project models a small social platform containing:

- Users
- Friend connections
- Liked pages / interests

The project processes this data and produces two recommendation-style outputs:

1. **People You May Know** — recommends users based on mutual-friend relationships.
2. **Pages You Might Like** — recommends pages using shared interests between users.

It also includes a dedicated cleaning workflow for common data-quality issues.

---

## 🚀 Key Features

### 1. Data Loading
- Reads structured JSON data.
- Displays users, connections, and pages.
- Uses reusable Python functions for file handling.

### 2. Data Cleaning
The cleaning workflow handles:
- Missing user names
- Duplicate friend IDs
- Inactive users
- Duplicate page IDs

### 3. People You May Know
The recommendation logic:
- Finds a user's direct friends.
- Looks at friends-of-friends.
- Excludes the current user and existing direct friends.
- Counts mutual connections.
- Ranks suggested users by mutual-friend count.

### 4. Pages You Might Like
The page recommendation logic:
- Compares users' liked pages.
- Measures shared interests.
- Scores pages that the target user has not already liked.
- Sorts recommendations by score.

---

## 🧠 Project Workflow

```text
Raw JSON Data
     │
     ▼
Data Loading
     │
     ▼
Data Cleaning
     │
     ├───────────────┐
     ▼               ▼
Friend Network     Page Interests
     │               │
     ▼               ▼
Mutual Friends     Shared Interests
     │               │
     ▼               ▼
People Suggestions Page Recommendations
```

---

## 📁 Repository Structure

```text
Coders-of-Delhi/
│
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── notebooks/
│   ├── 01_introduction.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_people_you_may_know.ipynb
│   └── 04_pages_you_might_like.ipynb
│
├── data/
│   ├── data.json
│   ├── data2.json
│   ├── massive_data.json
│   └── cleaned_data2.json
│
├── src/
│   └── recommendations.py
│
├── outputs/
│   ├── people_you_may_know_user_10.txt
│   └── page_recommendations_user_1.txt
│
└── docs/
    └── PROJECT_OVERVIEW.md
```

---

## 📊 Example Results

### People You May Know — User 10

The current recommendation workflow returns user IDs:

```text
11, 6, 4, 7, 14, 15, 18, 1, 2, 3, 13, 22
```

These are ranked using mutual-friend relationships.

### Pages You Might Like — User 1

The highest-scoring recommendations include:

```text
AI & ML Community      → score 2
Blockchain Innovators  → score 1
Cloud Computing Pros   → score 1
```

---

## 🛠️ Technologies

- Python
- JSON
- Jupyter Notebook
- Data Cleaning
- Set / Dictionary based relationship analysis
- Rule-based recommendation logic

No external Python package is required for the core scripts.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/coders-of-delhi.git
cd coders-of-delhi
```

### 2. Open the notebooks

Launch Jupyter Notebook / JupyterLab and open the files inside `notebooks/`.

### 3. Run the Python module

```bash
python src/recommendations.py
```

---

## 📌 Learning Outcomes

This project demonstrates practical understanding of:

- Reading and writing JSON
- Python functions
- Lists, sets, and dictionaries
- Data-quality handling
- Relationship/network-style analysis
- Basic recommendation logic
- Modularizing notebook logic into reusable Python code

---

## 🔮 Future Improvements

Possible next steps:

- Convert JSON data into Pandas DataFrames
- Add recommendation precision / evaluation metrics
- Build a graph visualization of user relationships
- Create a Streamlit dashboard
- Add a user-search interface
- Replace rule-based recommendations with graph-based or ML approaches
- Add automated tests
- Add larger real-world datasets

---

## 👨‍💻 Author

**Dinesh Chauhan**

B.Tech — Computer Science (Data Science & AI)

**Focus:** Data Science • Machine Learning • RAG • Python • SQL

