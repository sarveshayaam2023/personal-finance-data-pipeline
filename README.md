# personal-finance-data-pipeline

Overview

This project is an end-to-end personal finance data pipeline that ingests raw financial data from multiple sources, cleans and validates it, transforms it into an analytics-friendly star schema, and loads it into a data warehouse on a scheduled basis.

The pipeline is orchestrated using Apache Airflow and is designed with production-grade reliability, observability, and data quality checks in mind.

This project mirrors real-world data engineering systems used to support analytics and machine learning workflows.

Raw Data Sources
(API, CSV files)
        ↓
Data Ingestion (Python)
        ↓
Data Cleaning & Standardization
        ↓
Data Validation (Quality Checks)
        ↓
Data Transformation (Star Schema)
        ↓
Data Warehouse (PostgreSQL / DuckDB)
        ↓
Scheduled & Monitored via Airflow

# Key Features

Ingestion from multiple data sources (API + CSV)

Data cleaning and normalization

Schema and data quality validation

Star schema data modeling

Automated scheduling with Airflow

Failure handling and retries

Logging and observability

Designed to support downstream analytics and ML use cases

# Tech Stack

Python – ingestion, cleaning, orchestration logic

Apache Airflow – workflow orchestration and scheduling

SQL – transformations and data modeling

dbt – analytics engineering and transformations

Great Expectations – data quality validation

PostgreSQL / DuckDB – analytics data warehouse

Docker – local Airflow environment (via Astronomer)
