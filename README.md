# Student Performance Analysis

A small Python project that explores student marks with NumPy and presents the results in an interactive Streamlit dashboard.

## Features

- Analyses marks for five students across Maths, Python, ML, and English.
- Calculates subject averages, medians, mode, variance, and standard deviation.
- Identifies the best-average and most-consistent subjects.
- Classifies each student's overall performance.
- Shows correlations between Maths and Python, and Maths and ML.
- Displays individual marks, average score, performance category, and score trend.

## Requirements

- Python 3.9 or newer
- `numpy`
- `streamlit` (for the dashboard)

## Setup

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install numpy streamlit
```

## Run the dashboard

```bash
streamlit run app.py
```

Streamlit will print a local URL, normally `http://localhost:8501`. Open it in a browser to view the dashboard.

## Run the console report

```bash
python main.py
```

## Project structure

```text
.
├── app.py     # Interactive Streamlit dashboard
├── main.py    # Command-line analysis report
└── README.md
```

## Data

The project currently uses a small sample dataset defined directly in `app.py` and `main.py`. Each row represents a student (A–E), and each column represents a subject. Update the `students`, `subjects`, and `marks` arrays to analyse a different dataset.

## Technologies

- Python
- NumPy
- Streamlit
