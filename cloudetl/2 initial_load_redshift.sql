-- Drop Schema dwh_staging
CREATE SCHEMA dwh_staging

-- Drop Table dwh_staging.table1
CREATE TABLE dwh_staging.table1 (
  id INTEGER,
  foriegnkey1_id VARCHAR(32),
  datetime1 TIMESTAMP,
  datetime2 TIMESTAMP,
  status VARCHAR(11),
  name VARCHAR(100),
  description VARCHAR(200)
);


-- Drop Schema dwh
CREATE SCHEMA dwh

-- Drop Table dwh.table1
CREATE TABLE dwh.table1 (
  id INTEGER,
  foriegnkey1_id VARCHAR(32),
  datetime1 TIMESTAMP,
  datetime2 TIMESTAMP,
  status VARCHAR(11),
  name VARCHAR(100),
  description VARCHAR(200)
);

-- For this to work, in IAM, add S3 full access policy role (honRedshiftRole) being used.
-- So now you have the role able to access redshift and S3, you can do this...
copy dwh.table1 from 's3://honbucket2/table1/initialload/table1.csv'
iam_role 'arn:aws:iam::302907455183:role/honRedshiftRole'
CSV QUOTE '\"' DELIMITER ','
acceptinvchars;

Select * From dwh.table1 Order By id Asc Limit 100