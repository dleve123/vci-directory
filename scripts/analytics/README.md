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

```bash
$ streamlit run dashboard.py
```
