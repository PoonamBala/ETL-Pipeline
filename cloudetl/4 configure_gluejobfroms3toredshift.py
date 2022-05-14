import boto3,json
from pg import DB

# secret_name = 'your-secret-name'
region_name = 'eu-west-1'

session = boto3.session.Session()

# Secrets not working...
# client = session.client(service_name='secretsmanager',region_name=region_name)
# get_secret_value_response = cclient.get_secret_value(SecretID=secret_name)
# creds = json.loads(get_secret_value_response['SecretString'])

username = 'awsuser'
password = 'xxxxxxxxxx'
host = 'redshift-cluster-1.cpvdcihuxnee.eu-west-1.redshift.amazonaws.com'

db = DB(dbname='dev',host=host,port=5439,user=username,passwd=password)

merge_qry = """
			begin ;

			copy dwh_staging.table1 from 's3://honbucket2/table1/incrementalload/table1.csv'
			iam_role 'arn:aws:iam::302907455183:role/honRedshiftRole'
			CSV QUOTE '\"' DELIMITER ','
			acceptinvchars;

			delete
				from
					dwh.table1
				using dwh_staging.table1
				where dwh.table1.id = dwh_staging.table1.id;

			insert into dwh.table1 select * from dwh_staging.table1;

			truncate table dwh_staging.table1;

			end ;

			"""

result = db.query(merge_qry)
# print(result)