# Databricks notebook source
# MAGIC %run ./utils

# COMMAND ----------

import requests
from requests.auth import HTTPBasicAuth

# COMMAND ----------

def request_create_in(body):
    url = 'https://dev326303.service-now.com/api/now/table/incident'
    user = dbutils.secrets.get(scope = "servicenow", key = "user") 
    password = dbutils.secrets.get(scope = "servicenow", key = "password") 
    headerReq = {
        'Content-Type': 'application/json'
    }
    authReq = HTTPBasicAuth()
    res = requests.post(url, auth=authReq, header=headerReq, json=body)
    return res.status_code
