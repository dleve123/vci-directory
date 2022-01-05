import streamlit as st
import pandas as pd
import plotly.express as px

st.title("SMART Health Cards Analytics Dashboard")

issuer_count_data = pd.read_csv(
    "data/issuer_count_totals_over_time.csv",
    parse_dates=[0],
    infer_datetime_format=True,
)

issuer_count_fig = px.line(
    data_frame=issuer_count_data,
    line_shape="vh",
    x="commit_datetime",
    y="total_num_issuers",
    title="Number of issuers in VCI Directory over time",
)
issuer_count_fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Number of Issuers"
)

st.header("VCI Issuer Count")
st.plotly_chart(issuer_count_fig)
