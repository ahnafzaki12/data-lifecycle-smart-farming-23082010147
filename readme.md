# 🌱 Smart Agriculture Data Lifecycle Project

## 📌 Overview

This project analyzes a Smart Agriculture dataset containing **16,411 records** focusing on environmental factors affecting irrigation decisions.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Clean and validate dataset
- Calculate Data Quality Metrics
- Build interactive dashboard using Streamlit
- Deploy to cloud

---

## 📊 Dataset Information

| Feature | Description |
|---------|------------|
| crop_id | Unique crop identifier |
| soil_type | Type of soil |
| seedling_stage | Crop growth stage |
| moi | Moisture Index |
| temp | Temperature (°C) |
| humidity | Relative humidity (%) |
| result | Irrigation need (1 = Yes, 0 = No) |

---

## 🔄 Data Lifecycle Process

1. Data Collection  
2. Data Cleaning  
3. Exploratory Data Analysis (EDA)  
4. Data Quality Assessment  
5. Dashboard Development  

---

## 📈 Dashboard Visualizations

### 1️⃣ Time Series Irrigation Trend
Shows irrigation demand trend over time.

### 2️⃣ Gauge Meter (Average MOI)
Displays real-time agricultural moisture indicator.

### 3️⃣ Heatmap Alert System
Visualizes irrigation probability across soil type and seedling stage.

### 4️⃣ Temperature vs Irrigation Boxplot
Analyzes temperature distribution impact on irrigation needs.

---

## 🌐 Live Dashboard

👉 [Smart Agriculture Dashboard](https://data-lifecycle-smart-farming-23082010147-kazbvniijkwykv7oesnnj.streamlit.app/)

---

## 📂 Project Structure


repo_github/
│── README.md
│
├── data/
│ └── raw/
│ └── smart_agriculture_dataset.csv
│
├── Data_Lifecycle_Smart_Agriculture.ipynb
│
├── dashboard/
│ └── streamlit_app.py
│
└── outputs/
├── cleaned_data.csv
├── analysis_report.pdf
└── dashboard_screenshot.png


---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## 📊 Data Quality Metrics

- Accuracy  
- Completeness  
- Timeliness  
- Final Data Quality Score  

---

## 🚀 How to Run Locally

### 1️⃣ Install Dependencies


pip install -r requirements.txt


### 2️⃣ Run Streamlit App


streamlit run dashboard/streamlit_app.py


---

## 📄 Outputs Generated

- Cleaned dataset (`cleaned_data.csv`)
- Analysis report (`analysis_report.pdf`)
- Dashboard screenshot (`dashboard_screenshot.png`)

---

## 📄 License

Apache 2.0

---

## 👨‍💻 Author

**M. Ahnaf Zaki**  
Information Systems Student  
2026
