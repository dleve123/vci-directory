if __name__ == "__main__":
    # %%
    from IPython import get_ipython
    import pandas as pd
    import matplotlib.pyplot as plt

    # auto-reload deps
    get_ipython().run_line_magic('reload_ext', 'autoreload')
    get_ipython().run_line_magic('autoreload', '2')

    # %%
    data = pd.read_csv(
        'data/issuer_count_totals_over_time.csv',
        parse_dates=[0], infer_datetime_format=True
    )
    data.head()
    # %%
    import plotly.express as px

    fig = px.line(
        data_frame=data,
        line_shape='vh',
        x='commit_datetime',
        y='total_num_issuers',
        title='Number of issuers in VCI Directory over time',
    )
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Total Number of Issuers'
    )

    fig.show()
