# 🚀 Task Scheduler Optimization System

## 📌 Overview

The **Task Scheduler Optimization System** is a constraint-aware scheduling engine that assigns tasks to time slots in order to **maximize profit and minimize missed deadlines**.

This project combines:

* **Data Structures & Algorithms (Greedy + Heap)**
* **Optimization (Google OR-Tools CP-SAT Solver)**
* **System Design**
* **Interactive Dashboard (Streamlit)**

---

## 🎯 Problem Statement

In real-world systems (CPU scheduling, project management, cloud computing), tasks must be executed efficiently under constraints such as:

* Deadlines
* Execution time
* Priority
* Resource limits

This project solves the problem by:
✔ Selecting optimal tasks
✔ Minimizing missed deadlines
✔ Maximizing total profit

---

## 🧠 DSA Concepts Used

* ✅ Greedy Algorithm
* ✅ Priority Queue (Heap)
* ✅ Sorting (Multi-key)
* ✅ Simulation (Timeline)
* ✅ Optimization Modeling

---

## ⚙️ Features

### 🔹 Core Features

* Task input via CSV
* Deadline-based scheduling
* Profit maximization
* Missed task detection

### 🔹 Advanced Features

* CP-SAT Optimal Solver (OR-Tools)
* CLI Interface
* Multi-color dashboard charts
* File upload support
* Report generation (CSV + TXT)

---

## 🏗️ Project Architecture

```
Task Input → Sorting → Heap → Greedy Scheduling
       ↓
   Timeline Generation
       ↓
Performance Analysis
       ↓
Reports + Dashboard Visualization
```

---

## 📁 Folder Structure

```
Task-Scheduler-Optimization-System/
│
├── data/                # Input datasets
├── src/                 # Core logic
├── dashboard/           # Streamlit UI
├── outputs/             # Generated reports
├── images/              # Screenshots
│
├── main.py              # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 🔹 1. Clone Repository

```
git clone https://github.com/YuvaKarthikeswarDadisetty/Task-Scheduler-Optimization-System
cd Task-Scheduler-Optimization-System
```

### 🔹 2. Setup Environment

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install plotly
```

### 🔹 3. Run CLI (DSA Logic)

```
python main.py
```

### 🔹 4. Run Dashboard (UI)

```
streamlit run dashboard/app.py
```

Open:

```
http://localhost:8501
```

---

## 📊 Sample Output

### ✅ CLI Output

* Sorted tasks
* Optimized schedule
* Total profit
* Missed tasks

### 📁 Generated Files

```
outputs/
├── timeline.csv
├── missed_tasks.csv
└── summary.txt
```

---

## 📸 Screenshots

### 🚀 Dashboard

![Dashboard](images/)

### 📊 Charts

![Charts](images/)

### 💻 CLI Output

![CLI](images/)

---

## 🧪 Example Use Case

* Project Management
* Cloud Resource Scheduling
* CPU Scheduling
* Manufacturing Job Scheduling

---

## 🔥 Why This Project Stands Out

* Combines **DSA + Optimization + UI**
* Real-world system design
* Interactive visualization
* Recruiter-friendly

---

## 📈 Future Improvements

* Multi-resource scheduling
* Real-time task updates
* AI-based prediction
* Deployment (Streamlit Cloud)

---

## 👨‍💻 Author

**Yuva Karthikeswar Dadisetty**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
