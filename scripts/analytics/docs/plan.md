# VCI Directory Analytics Plan

## Document Purpose

This document intends to serve as an open, concise and actionable plan for the VCI analytics project.

## Vision

The current end goal of this project is provide transparent, privacy-preserving,
and compelling data and visualizations on the deployment of SMART Health Cards
for VCI Issuers.  Such data and visualizations could help identify trends,
inform policy decisions, and serve as a system of record for VCI.

## Technical State

### Current State

This fork of the the-commons-project/vci-directory contains the analytics
"sub-project" (similar to the vci-directory-auditor sub-project) that enables
the _non automated_ refreshing of 2 datasets: (1) count of VCI issuers over time
(via the Git history) and (2) count of VCI issuers by US state. Instructions for
how to refresh these data are documented in scripts/analytics/README.md

The [data visualization app][streamlit-app-link], powered by [Streamlit](https://streamlit.io/), is
automatically updated on pushes to the `count-by-state` branch of this fork.

### Future State

The proximate (and hopefully achievable) technical goals for this analytics project
are to have:

1. Automatic refreshing of data
2. Collective ownership of the analytics dashboard (not tied to a personal account)
3. Production-ready dashboard deployment

Given this, the following actions need to happen.

### Tactical Next Steps

- [ ] Collective ownership of source code
  - Recommendation: Merge this fork's branch into upstream repository
  - Alternative: Migrate fork to a separate repo within the dvci or
    the-commons-project namespace.
- [ ] Enable automatic refreshing of data
  - Recommendation:
    - Run Python refresh scripts via Github actions on merge to `main`.
    - Persist updated data files to a `data` Git branch  committed by an robot
      user for ease of audit.
        - Alternative: Push data to some object store like AWS S3 (introduces some
        system complexity over Github alternative I believe)
- [ ] Update dashboard deployment
    -  Evaluate/pay for Streamlit cloud hosting or deploy to some VCI-member
    infrastructure
      - [Dockerfile example][dockerfile-example]
    - Change references to raw data locations depending upon implementation of deployment platform.
    - Change continuous deployment setup (automatic dashboard deployment) to
      align with deployment platform.

[streamlit-app-link]:https://share.streamlit.io/dleve123/vci-directory/count-by-state/scripts/analytics/dashboard.py
[dockerfile-example]:https://github.com/collinprather/streamlit-docker/blob/master/Dockerfile
