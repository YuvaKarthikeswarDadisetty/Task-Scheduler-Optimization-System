import sys
import os

# ✅ FIX IMPORT PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.input_handler import load_tasks_from_csv
from src.scheduler import sort_tasks, greedy_schedule
from src.analyzer import generate_timeline, calculate_performance
from src.cp_sat_solver import solve_with_cp_sat


# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Task Scheduler Dashboard",
    layout="wide"
)

# --------------------------
# DARK MODE
# --------------------------
st.markdown("""
<style>
body {background-color: #0E1117; color: white;}
.card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Task Scheduler Optimization Dashboard")


# --------------------------
# SIDEBAR
# --------------------------
st.sidebar.header("⚙️ Configuration")

uploaded_file = st.sidebar.file_uploader("📂 Upload Task CSV", type=["csv"])

file_path = st.sidebar.text_input(
    "OR Enter CSV Path",
    value="data/tasks.csv"
)

run_button = st.sidebar.button("🚀 Run Optimization")


# --------------------------
# LOAD DATA
# --------------------------
def load_data():
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        from src.task import Task

        tasks = []
        for _, row in df.iterrows():
            tasks.append(Task(
                row["name"],
                row["deadline"],
                row["duration"],
                row["profit"],
                row["priority"]
            ))
        return tasks
    else:
        return load_tasks_from_csv(file_path)


# --------------------------
# MAIN
# --------------------------
if run_button:

    tasks = load_data()

    if not tasks:
        st.error("❌ No tasks loaded!")
        st.stop()

    # Greedy
    sorted_tasks = sort_tasks(tasks)
    greedy_tasks = greedy_schedule(sorted_tasks)
    timeline = generate_timeline(greedy_tasks)
    profit, missed = calculate_performance(tasks, greedy_tasks)

    # Optimal
    optimal_tasks = solve_with_cp_sat(tasks)
    optimal_profit = sum(t.profit for t in optimal_tasks)

    # --------------------------
    # KPI CARDS
    # --------------------------
    col1, col2, col3 = st.columns(3)

    col1.markdown(f"<div class='card'><h3>💰 Greedy Profit</h3><h1>{profit}</h1></div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='card'><h3>🧠 Optimal Profit</h3><h1>{optimal_profit}</h1></div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='card'><h3>❌ Missed Tasks</h3><h1>{len(missed)}</h1></div>", unsafe_allow_html=True)

    st.divider()

    # --------------------------
    # TASK TABLE
    # --------------------------
    st.subheader("📋 Task Data")
    df = pd.DataFrame([vars(t) for t in tasks])
    st.dataframe(df, use_container_width=True)

    st.divider()

    # --------------------------
    # 🎨 MULTI-COLOR TIMELINE
    # --------------------------
    st.subheader("⏱️ Execution Timeline")

    timeline_df = pd.DataFrame(
        timeline, columns=["Task", "Start", "End"]
    )

    fig1 = px.bar(
        timeline_df,
        x="Task",
        y="End",
        color="Task",  # 🔥 MULTI COLOR
        text="End",
        title="Execution Timeline"
    )

    fig1.update_layout(
        template="plotly_dark"
    )
    fig1.update_traces(marker_line_width=1.5, opacity=0.9)
    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # --------------------------
    # 🎨 PROFIT COMPARISON
    # --------------------------
    st.subheader("📊 Profit Comparison")

    profit_df = pd.DataFrame({
        "Method": ["Greedy", "Optimal"],
        "Profit": [profit, optimal_profit]
    })

    fig2 = px.bar(
        profit_df,
        x="Method",
        y="Profit",
        color="Method",  # 🔥 MULTI COLOR
        text="Profit"
    )

    fig2.update_layout(template="plotly_dark")

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # --------------------------
    # 🎨 COMPLETION ANALYSIS
    # --------------------------
    st.subheader("📈 Task Completion Analysis")

    completion_df = pd.DataFrame({
        "Status": ["Completed", "Missed"],
        "Count": [len(greedy_tasks), len(missed)]
    })

    fig3 = px.bar(
        completion_df,
        x="Status",
        y="Count",
        color="Status",  # 🔥 MULTI COLOR
        text="Count"
    )

    fig3.update_layout(template="plotly_dark")

    st.plotly_chart(fig3, use_container_width=True)

    st.success("✅ Optimization Completed Successfully!")