# Ghana-Stock-Exchange-Data-Pipeline
## Data Pipeline with GSE API,Pandas, Airflow, Amazon EC2 ans Amazon S3

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Stocks data into AWS S3 . The pipeline leverages a combination of tools and services including Apache Airflow, Pandas, Amazon S3 and Amazon EC2.

## Overview
The pipeline is designed to:

- Extract data from GSE using its API.
- Transform the data using the Python library Pandas.
- Orchestrate the data workflow using Apache Airflow running on an Amazon EC2 instance.
- Load the transformed data into Amazon S3.
