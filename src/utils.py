# Databricks notebook source
from datetime import datetime

# COMMAND ----------

def app_log(level, message):
    print(f'{datetime.now().strftime("%m/%d/%Y %H:%M:%S")} - {level.upper()}: {message}')
