# Ghana-Stock-Exchange-Data-Pipeline
## Data Pipeline with GSE API,Pandas, Airflow, Amazon EC2 and Amazon S3

This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Stocks data into AWS S3 . The pipeline leverages a combination of tools and services including Apache Airflow, Pandas, Amazon S3 and Amazon EC2.

## Overview
The pipeline is designed to:

- Extract data from GSE using its API.
- Transform the data using the Python library Pandas.
- Orchestrate the data workflow using Apache Airflow running on an Amazon EC2 instance.
- Load the transformed data into Amazon S3.

## Architecture
![Architecture Diagram](https://github.com/BQuophi/Ghana-Stock-Exchange-Data-Pipeline/assets/92530942/08c2b08a-41dd-48b1-bbd7-f08a8599349c)

1. GSE API: Source of the data.
2. Pandas : Data Transformation Tool
3. Apache Airflow: Orchestrates the ETL process.
4. Amazon EC2 : Create an instance on which Aiflow runs
5. Amazon S3: Raw data storage.

## Prerequisites
- AWS Account with appropriate permissions for EC2 and S3.
- GSE API access.
- Python 3.9 or higher

