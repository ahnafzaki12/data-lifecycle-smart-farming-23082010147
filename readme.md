🌱 Smart Agriculture Data Lifecycle Project
📌 Project Overview

This project implements an end-to-end Data Lifecycle framework on a Smart Agriculture dataset containing 16,411 crop records.

The analysis focuses on understanding how environmental conditions such as:

Soil Type

Seedling Stage

Moisture Index (MOI)

Temperature

Humidity

influence irrigation decisions (result: 1 = irrigation needed, 0 = not needed).

The project covers the full data pipeline from raw data processing to interactive dashboard deployment using Streamlit.

🎯 Objectives

Perform comprehensive Exploratory Data Analysis (EDA)

Clean and validate dataset quality

Calculate Data Quality Metrics

Generate actionable agricultural insights

Develop an interactive Smart Farming dashboard

Deploy the dashboard to the cloud

📊 Dataset Information

Total Records: 16,411

Features: 7 main variables

License: Apache 2.0

Usability Score: 5.29

Features Description
Feature	Description
crop_id	Unique crop identifier
soil_type	Type of soil (Black Soil, Red Soil, etc.)
seedling_stage	Crop growth stage
moi	Moisture Index (soil moisture level)
temp	Temperature (°C)
humidity	Relative humidity (%)
result	Irrigation requirement (1 = Yes, 0 = No)
🔄 Data Lifecycle Process

This project follows a structured Data Lifecycle:

1️⃣ Data Collection

Dataset loaded from raw CSV format.

2️⃣ Data Cleaning

Missing value handling

Duplicate removal

Column standardization

Data type validation

3️⃣ Exploratory Data Analysis (EDA)

Statistical summary

Distribution analysis

Categorical frequency analysis

Correlation analysis

4️⃣ Data Quality Assessment

The following metrics were calculated:

Accuracy
1 - (missing values / total values)

Completeness
(non-null values / total values)

Timeliness
% of data within last 30 days

Final Data Quality Score
Average of all three metrics

5️⃣ Dashboard Visualization

Interactive analytics built using Streamlit + Plotly.

📈 Dashboard Features

The dashboard includes at least 4 core visualizations:

📅 1. Time Series Analysis

Shows irrigation demand trends over time.

📟 2. Gauge Meter

Displays:

Average Moisture Index (MOI)

Real-time agricultural indicator

🔥 3. Heatmap Alert System

Visualizes irrigation risk level across:

Soil Type

Seedling Stage

Red intensity indicates higher irrigation probability.

🌡 4. Temperature vs Irrigation Boxplot

Analyzes temperature distribution impact on irrigation needs.

🌐 Live Dashboard

Access the deployed Streamlit dashboard here:

👉 Smart Agriculture Dashboard

📂 Project Structure
repo_github/
│── README.md
│
├── data/
│   └── raw/
│       └── smart_agriculture_dataset.csv
│
├── Data_Lifecycle_Smart_Agriculture.ipynb
│
├── dashboard/
│   └── streamlit_app.py
│
└── outputs/
    ├── cleaned_data.csv
    ├── analysis_report.pdf
    └── dashboard_screenshot.png
🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Plotly

Streamlit

🚀 How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Run Streamlit App
streamlit run dashboard/streamlit_app.py
📑 Outputs Generated

Cleaned dataset (cleaned_data.csv)

Analysis report (analysis_report.pdf)

Dashboard screenshot (dashboard_screenshot.png)

Live deployed dashboard

📌 Key Insights

Soil type significantly influences irrigation requirement.

Higher temperature correlates with increased irrigation probability.

Certain seedling stages require more frequent watering.

Data quality score indicates dataset reliability for predictive modeling.

🔐 License

This dataset and project follow the Apache 2.0 License.

👨‍💻 Author

M. Ahnaf Zaki
Information Systems Student
Smart Agriculture Data Lifecycle Project
2026
