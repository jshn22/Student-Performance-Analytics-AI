import streamlit as st
import numpy as np


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .main {
        padding-top: 2rem;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ddd;
        background-color: #ffffff;
        text-align: center;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    }

    .card-title {
        color: #777;
        font-size: 14px;
    }

    .card-value {
        font-size: 25px;
        font-weight: 700;
        margin-top: 5px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 650;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .performance-card {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATA
# =========================================================

students = np.array(["A", "B", "C", "D", "E"])

subjects = np.array([
    "Maths",
    "Python",
    "ML",
    "English"
])

marks = np.array([
    [80, 85, 78, 75],
    [65, 70, 68, 72],
    [90, 92, 88, 85],
    [55, 60, 58, 65],
    [75, 80, 72, 78]
])


# =========================================================
# CALCULATIONS
# =========================================================

# Subject average
avgmarks = np.mean(marks, axis=0)

# Median
mediann = np.median(marks, axis=0)

# Mode
value, count = np.unique(marks, return_counts=True)
mode = value[np.argmax(count)]

# Variance
variance = np.var(marks, axis=0)

# Standard deviation
std = np.std(marks, axis=0)

# Best subject
best_subject = subjects[np.argmax(avgmarks)]

# Highest variance subject
highest_variance_subject = subjects[np.argmax(variance)]
highest_variance_value = np.max(variance)

# Most consistent subject
consistent_subject = subjects[np.argmin(std)]

# Student averages
student_avg = np.mean(marks, axis=1)


# =========================================================
# FUNCTIONS
# =========================================================

def get_performance(avg):

    if avg >= 85:
        return "Excellent"

    elif avg >= 75:
        return "Good"

    elif avg >= 65:
        return "Average"

    else:
        return "Needs Improvement"


def correlation(cor):

    if cor >= 0.7:
        return "Strong Positive Correlation"

    elif cor >= 0.3:
        return "Moderate Positive Correlation"

    elif cor > -0.3:
        return "Weak or No Correlation"

    elif cor > -0.7:
        return "Moderate Negative Correlation"

    else:
        return "Strong Negative Correlation"


def performance_trend(student_marks):

    changes = np.diff(student_marks)

    if np.all(changes > 0):
        return "Improving"

    elif np.all(changes == 0):
        return "Stable"

    elif np.all(changes < 0):
        return "Decreasing"

    else:
        return "Fluctuating"


# Correlations
mathm = marks[:, 0]
pythonm = marks[:, 1]
ml = marks[:, 2]

math_py = np.corrcoef(mathm, pythonm)[0, 1]
math_ml = np.corrcoef(mathm, ml)[0, 1]


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🎓 Student Performance Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze student performance using Python & NumPy</div>',
    unsafe_allow_html=True
)


# =========================================================
# OVERVIEW CARDS
# =========================================================

st.markdown(
    '<div class="section-title">📌 Overview</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍🎓 Total Students",
        students.shape[0]
    )

with col2:
    st.metric(
        "📚 Total Subjects",
        subjects.shape[0]
    )

with col3:
    st.metric(
        "🏆 Best Subject",
        best_subject
    )

top_student_index = np.argmax(student_avg)

with col4:
    st.metric(
        "⭐ Top Student",
        f"Student {students[top_student_index]}"
    )


# =========================================================
# SUBJECT ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">📚 Subject Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🏆 Best Average Subject")

    st.info(
        f"**{best_subject}** has the highest average marks."
    )

    st.markdown("### 📊 Median Marks")

    median_table = {
        "Subject": subjects,
        "Median": mediann
    }

    st.dataframe(
        median_table,
        use_container_width=True,
        hide_index=True
    )

with col2:

    st.markdown("### 📈 Variance")

    variance_table = {
        "Subject": subjects,
        "Variance": variance
    }

    st.dataframe(
        variance_table,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        f"Highest Variance: **{highest_variance_subject} "
        f"({highest_variance_value:.1f})**"
    )

    st.success(
        f"Most Consistent Subject: **{consistent_subject}**"
    )


# =========================================================
# SUBJECT PERFORMANCE CHART
# =========================================================

st.markdown(
    '<div class="section-title">📊 Average Marks by Subject</div>',
    unsafe_allow_html=True
)

chart_data = {
    "Subject": subjects,
    "Average Marks": avgmarks
}

st.bar_chart(
    chart_data,
    x="Subject",
    y="Average Marks"
)


# =========================================================
# MODE
# =========================================================

st.markdown(
    '<div class="section-title">🔢 Mode</div>',
    unsafe_allow_html=True
)

st.metric(
    "Most Frequently Occurring Mark",
    mode
)


# =========================================================
# CORRELATION
# =========================================================

st.markdown(
    '<div class="section-title">🔗 Correlation Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Maths ↔ Python")

    st.metric(
        "Correlation",
        f"{math_py:.2f}"
    )

    st.success(
        correlation(math_py)
    )


with col2:

    st.markdown("### Maths ↔ ML")

    st.metric(
        "Correlation",
        f"{math_ml:.2f}"
    )

    st.success(
        correlation(math_ml)
    )


# =========================================================
# STUDENT ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">👨‍🎓 Student Analysis</div>',
    unsafe_allow_html=True
)

student_data = []

for i in range(len(students)):

    avg = student_avg[i]

    performance = get_performance(avg)

    student_data.append({
        "Student": f"Student {students[i]}",
        "Average Marks": round(avg, 2),
        "Performance": performance
    })


st.dataframe(
    student_data,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# INDIVIDUAL STUDENT DETAILS
# =========================================================

st.markdown(
    '<div class="section-title">👤 Individual Student</div>',
    unsafe_allow_html=True
)

selected_student = st.selectbox(
    "Select a student",
    students,
    format_func=lambda x: f"Student {x}"
)

student_index = np.where(students == selected_student)[0][0]

selected_marks = marks[student_index]

selected_average = student_avg[student_index]

selected_performance = get_performance(selected_average)

selected_trend = performance_trend(selected_marks)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Score",
        f"{selected_average:.2f}"
    )

with col2:
    st.metric(
        "Performance",
        selected_performance
    )

with col3:
    st.metric(
        "Performance Trend",
        selected_trend
    )


st.markdown("### 📚 Subject Scores")

selected_subject_data = {
    "Subject": subjects,
    "Marks": selected_marks
}

st.bar_chart(
    selected_subject_data,
    x="Subject",
    y="Marks"
)


# =========================================================
# PERFORMANCE TREND
# =========================================================

st.markdown(
    '<div class="section-title">📈 Performance Trend</div>',
    unsafe_allow_html=True
)

trend_data = []

for i in range(len(students)):

    trend = performance_trend(marks[i])

    trend_data.append({
        "Student": f"Student {students[i]}",
        "Trend": trend
    })


st.dataframe(
    trend_data,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Built with Python • NumPy • Streamlit"
)