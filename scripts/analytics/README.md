# VCI Directory Analytics

This directory contains code that collects, stores and visualizes summary
statistics regarding VCI SHC issuers.


## Data Collection

### Issuer Counting

To regenerate the series of VCI issuer counts over time, run `count_issuers.py`
from the root of the vci-directory.

```bash
$ python scripts/analytics/count_issuers.py \
  vci-issuers.json > \
  scripts/analytics/data/issuer_count_totals_over_time.csv
```

## Data Visualization

We use [streamlit](https://streamlit.io/) as a Python-based dashboarding tool.

To run the streamlit dashboard locally _from `scripts/analytics`_:

### Secrets Configuration

We currently use Streamlit secrets to manage (not secret) configuration to
data files (CSVs and JSON files). However, to align with best practices,
we still don't version the local secrets manifest at `.streamlit/secrets.toml`
(required to boot the streamlit app).

As such, copy from the example secrets:

```bash
$ cp .streamlit/secrets.example.toml .streamlit/secrets.toml
```

```bash
$ streamlit run dashboard.py
```
