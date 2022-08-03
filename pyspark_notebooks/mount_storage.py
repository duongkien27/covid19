# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "3984387b-355f-4da4-a1a7-44ba9e651725",
           "fs.azure.account.oauth2.client.secret": "CgG8Q~4bf2ck2FjKv0PU6xk4D~fKah~X127jLce7",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/06f1b89f-07e8-464f-b408-ec1b45703f31/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@covidreportdldk.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportdldk/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covidreportdldk.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportdldk/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covidreportdldk.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportdldk/lookup",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/covidreportdldk/lookup")

# COMMAND ----------


