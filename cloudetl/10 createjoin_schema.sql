create external schema dwh_external_data_spectrum from data catalog 
database 'ecommerce_external_data' 
iam_role 'YOUR_ARN' 
region 'eu-west-1';


create external table dwh_external_data_spectrum.user_data_file(
	session_id varchar(255),
	event_timestamp varchar(150),
	event_type varchar(50),
	userid varchar(255),
	product_id varchar(255),
	category_id varchar(255)
)
row format delimited
fields terminated by ','
stored as textfile 
location 's3://BUCKET_NAME/user_behaviour/'
table properties ('skip.header.line.count'='1')

select 
	b.product_category_name_english ,
	a.year,
	count(1) as view_count
from 
	dwh_external_data_spectrum.parquet_output a 
join 
	mysql_dwh.product_category_name_translation b 
on
	a.category_id = b.product_category_name
where a.event_type = 'view'
group by 1,2
order by a.year 