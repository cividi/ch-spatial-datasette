# Swiss Spatial Datasette

[![Fetch latest data and deploy with Datasette](https://github.com/cividi/ch-spatial-datasette/workflows/Fetch%20latest%20data%20and%20deploy%20with%20Datasette/badge.svg)](https://github.com/cividi/ch-spatial-datasette/actions?query=workflow%3A%22Fetch+latest+data+and+deploy+with+Datasette%22)

Deploys a Datasette instance with data from the following sources:

* https://github.com/cividi/ch-municipalities

The Datasette instance lives at https://datasette.cividi.tech/ and is updated hourly using [a scheduled GitHub Action](https://github.com/cividi/ch-spatial-datasette/blob/main/.github/workflows/scheduled.yml).

More about this project on our blog: WIP

This repository is forked, with kind thanks, from https://github.com/simonw/covid-19-datasette/

Uses the deployment pattern described in [Deploying a data API using GitHub Actions and Cloud Run](https://simonwillison.net/2020/Jan/21/github-actions-cloud-run/).

## Using this data responsibly

Please **do not** use this tool to share information about COVID-19 without making absolutely sure you understand how the data is structured and sourced.

Recommended reading:

* [Why It’s So Freaking Hard To Make A Good COVID-19 Model](https://fivethirtyeight.com/features/why-its-so-freaking-hard-to-make-a-good-covid-19-model/)
* [Ten Considerations Before You Create Another Chart About COVID-19](https://medium.com/nightingale/ten-considerations-before-you-create-another-chart-about-covid-19-27d3bd691be8)
