# Getting Started
Follow the tutorial [here](https://github.com/microsoft/MLOpsPython/blob/master/docs/getting_started.md) until the **Create an Azure DevOps Service Connection for the Azure ML Workspace** step. The required .yml file can be found in this repository.

# First Data Ingestion
Run YS-First-Ingestion.yml the same way the environment setup was done. This pipeline will run a Python script which registers two datasets: aviation_main.csv and aviation_inflow.csv, both of which can be found under the data subfolder. 

# Continuous Integration
Next, run 