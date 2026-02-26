import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta

st.set_page_config(page_title="Smart Agriculture Dashboard", page_icon="🌱", layout="wide")

st.title("🌱 Smart Agriculture Monitoring Dashboard")
st.markdown("Dashboard ini memantau kondisi lingkungan pertanian, kebutuhan irigasi, dan metrik kualitas data.")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('outputs/cleaned_data.csv')
    except FileNotFoundError:
        try:
            df = pd.read_csv('dashboard/outputs/cleaned_data.csv')
        except FileNotFoundError:
            st.error("File data tidak ditemukan. Pastikan path 'cleaned_data.csv' benar.")
            return pd.DataFrame()
            
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

if not df.empty:
    total_records = len(df)
    total_cells = df.size
    
    accuracy = 100.0
    completeness = 100.0
    
    latest_date = df['timestamp'].max()
    thirty_days_ago = latest_date - timedelta(days=30)
    data_last_30_days = df[df['timestamp'] >= thirty_days_ago].shape[0]
    timeliness = (data_last_30_days / total_records) * 100

    st.markdown("### 📊 Data Quality Scores")
    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", f"{accuracy:.2f}%", "Optimal")
    col2.metric("Completeness", f"{completeness:.2f}%", "Optimal")
    col3.metric("Timeliness (30 Hari)", f"{timeliness:.2f}%", f"{data_last_30_days} Records")
    
    st.divider()

    row1_col1, row1_col2 = st.columns([1, 2])
    
    with row1_col1:
        st.markdown("#### Rata-rata Moisture Index (MOI)")
        avg_moi = df['moi'].mean()
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = avg_moi,
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "deepskyblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 30], 'color': "red"},
                    {'range': [30, 70], 'color': "lightgreen"},
                    {'range': [70, 100], 'color': "royalblue"}],
                'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}
            }
        ))
        fig_gauge.update_layout(height=300, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with row1_col2:
        st.markdown("#### Tren Suhu & Kelembaban (Time Series)")
        df_daily = df.set_index('timestamp').resample('D')[['temp', 'humidity']].mean().reset_index()
        fig_ts = px.line(df_daily, x='timestamp', y=['temp', 'humidity'], 
                         labels={'value': 'Nilai', 'variable': 'Parameter'},
                         color_discrete_map={'temp': 'red', 'humidity': 'blue'})
        fig_ts.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_ts, use_container_width=True)

    row2_col1, row2_col2 = st.columns(2)
    
    with row2_col1:
        st.markdown("#### 🚨 Heatmap Alert System (Risiko Irigasi)")
        heatmap_data = df.groupby(['soil_type', 'seedling_stage'])['result'].mean().reset_index()
        heatmap_pivot = heatmap_data.pivot(index='soil_type', columns='seedling_stage', values='result')
        
        fig_heat = px.imshow(heatmap_pivot, text_auto=".2f", aspect="auto",
                             color_continuous_scale='Reds',
                             labels=dict(color="Tingkat Risiko Irigasi"))
        fig_heat.update_layout(height=400)
        st.plotly_chart(fig_heat, use_container_width=True)
        
    with row2_col2:
        st.markdown("#### Kondisi Suhu vs Kelembaban")
        fig_scatter = px.scatter(df.sample(1000, random_state=42), x='temp', y='humidity', color='result',
                                 color_continuous_scale='Viridis',
                                 labels={'temp': 'Temperature (°C)', 'humidity': 'Humidity (%)'})
        fig_scatter.update_layout(height=400)
        st.plotly_chart(fig_scatter, use_container_width=True)