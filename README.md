# Code Challenge
Solution for Indicium code challenge

## The Challenge

The challenge is to build a pipeline that extracts data from two sources (a Postgres database and a CSV file) and writes the data first to local disk and then to a database of my choice. The pipeline should run daily and the data should be separated by source, table and execution day. The final goal is to be able to run a query that shows the orders and its details.

The pipeline will look something like this:

![image](https://user-images.githubusercontent.com/49417424/105993225-e2aefb00-6084-11eb-96af-3ec3716b151a.png)

## Requirements

- All tasks should be idempotent, you should be able the whole pipeline for a day and the result should be always the same
- Step 2 depends on both tasks of step 1, so you should not be able to run step 2 for a day if the tasks from step 1 did not succeed
- You should extract all the tables from the source database, it does not matter that you will not use most of them for the final step.
- You should be able to tell where the pipeline failed clearly, so you know from which step you should rerun the pipeline
- You have to provide clear instructions on how to run the whole pipeline. The easier the better.
- You have to provide a csv or json file with the result of the final query at the final database.
- You dont have to actually schedule the pipeline, but you should assume that it will run for different days.
- Your pipeline should be prepared to run for past days, meaning you should be able to pass an argument to the pipeline with a day from the past, and it should reprocess the data for that day. Since the data for this challenge is static, the only difference for each day of execution will be the output paths.

## Setup

With docker compose installed run

```
docker-compose up
```
Access http://localhost:8080
Username: airflow
Password: airflow

Unpause the DAG code_challenge

## References

Airflow is an open-source platform for developing, scheduling, and monitoring workflows
```
https://airflow.apache.org/docs/

```

Pandas is a open source data analysis and manipulation tool
```
https://airflow.apache.org/docs/

```

Sqlite3 provides a lightweight disk-based database
```
https://docs.python.org/3/library/sqlite3.html

```
