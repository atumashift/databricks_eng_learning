# Databricks notebook source
# MAGIC %run ../../Includes/_common

# COMMAND ----------

lesson_config = LessonConfig(name = None,
                             create_schema = True,
                             create_catalog = False,
                             requires_uc = False,
                             installing_datasets = True,
                             enable_streaming_support = False)

DA = DBAcademyHelper(course_config=course_config,
                     lesson_config=lesson_config)
DA.reset_lesson()
DA.init()
DA.conclude_setup()

# COMMAND ----------

# TODO
my_name = "Allison"

# COMMAND ----------

example_df = spark.range(16)


# COMMAND ----------

display(example_df)

# COMMAND ----------


