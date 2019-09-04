
-- metadata table database create statement

CREATE DATABASE IF NOT EXISTS metadata_job_details_db;

-- use metadata database
USE metadata_job_details_db;

-- metadata table create statement

CREATE TABLE IF NOT EXISTS metadata_job_details_tb(
    job_execution_date DATETIME,
    last_modified_column VARCHAR(50),
    last_modified_value VARCHAR(50),
    no_record_processed BIGINT,
    job_execution_status VARCHAR(20),
    job_start_time DATETIME,
    job_end_time DATETIME,
    batch_id VARCHAR(20)
);