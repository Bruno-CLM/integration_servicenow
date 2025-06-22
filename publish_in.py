# Databricks notebook source
# MAGIC %run ./_setup

# COMMAND ----------

# MAGIC %run ./get_keys

# COMMAND ----------

# MAGIC %run ./utils

# COMMAND ----------

import pika, json

# COMMAND ----------

def init_connection_rabitmq():
    parameters = pika.URLParameters(url_amqp)
    connection = pika.BlockingConnection(parameters)
    return connection

# COMMAND ----------

def finish_connection_rabitmq(connection):
    connection.close()

# COMMAND ----------

def publish_message_in_queue(message):
    connection = None
    try:
        connection = init_connection_rabitmq()
        channel = connection.channel()
        channel.basic_publish(
            exchange = '',
            routing_key = queue,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2,)
        )
        app_log('info', 'error enviando para fila ms.errors com sucesso')
    except Exception as e:
        app_log('error', e)
    finally:
        if connection:
            finish_connection_rabitmq(connection)
        
