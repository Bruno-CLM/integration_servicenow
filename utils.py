# Databricks notebook source
def app_log(level, message):
    print(f'{datetime.now().strftime("%m/%d/%Y %H:%M:%S")} - {level.upper()}: {message}')
