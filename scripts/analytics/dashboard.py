import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("SMART Health Cards Analytics Dashboard")

issuer_count_data = pd.read_csv(
    "data/issuer_count_totals_over_time.csv",
    parse_dates=[0],
    infer_datetime_format=True,
)

with open("data/issuers_by_state.json") as issuers_by_state_file:
    issuers_by_state_data = json.load(issuers_by_state_file)

issuer_count_fig = px.line(
    data_frame=issuer_count_data,
    line_shape="vh",
    x="commit_datetime",
    y="total_num_issuers",
    title="Number of issuers in VCI Directory over time",
)
issuer_count_fig.update_layout(
    xaxis_title="Date", yaxis_title="Total Number of Issuers"
)

st.header("VCI Issuer Count")
st.plotly_chart(issuer_count_fig)

st.header("US Issuer Coverage")

issuers_count_by_state = [len(issuers) for state, issuers in issuers_by_state_data.items()]
issuers_by_state_map_fig = go.Figure(
    data=go.Choropleth(
        locations=list(issuers_by_state_data.keys()),
        z=issuers_count_by_state,
        locationmode="USA-states",
        colorscale="Greens",
        colorbar_title="Count of VCI Issuers",
    )
)

# counts can only be an integer, so enforce that distance between ticks is 1
issuers_by_state_map_fig.update_traces(colorbar_dtick=1)
issuers_by_state_map_fig.update_layout(
    geo_scope='usa',
)
st.plotly_chart(issuers_by_state_map_fig)
