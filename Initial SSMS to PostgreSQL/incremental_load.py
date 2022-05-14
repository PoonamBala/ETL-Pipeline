from sqlalchemy import create_engine
import pandas as pd
import pyodbc
import os
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
driver = "{SQL Server Native Client 11.0}"
server = "localhost"
database = "AdventureWorksDW2017;"
src_conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + '\SQLEXPRESS' + ';DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd)
engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/AdventureWorks')

#read
source = pd.read_sql_query(""" SELECT top 10
CustomerKey,GeographyKey,CustomerAlternateKey,Title,FirstName,MiddleName,LastName,NameStyle,BirthDate,MaritalStatus
FROM dbo.DimCustomer; """, src_conn)
source

#save data
tbl_name = "stg_IncrementalLoadTest"
source.to_sql(tbl_name, engine, if_exists='replace', index=False)

#read target
target = pd.read_sql('Select * from public."stg_IncrementalLoadTest"', engine)
target

#select 2 rows for now
source = pd.read_sql_query(""" SELECT top 12
CustomerKey,GeographyKey,CustomerAlternateKey,Title,FirstName,MiddleName,LastName,NameStyle,BirthDate,MaritalStatus
FROM dbo.DimCustomer; """, src_conn)
source

#sample update
source.loc[source.MiddleName =='G', ['MiddleName']] = 'Gina'
source

#DETECT ALL THE CHANGES
target.apply(tuple,1)
source.apply(tuple,1).isin(target.apply(tuple,1))
changes = source[~source.apply(tuple,1).isin(target.apply(tuple,1))]
changes
modified = changes[changes.CustomerKey.isin(target.CustomerKey)]
modified
inserts = changes[~changes.CustomerKey.isin(target.CustomerKey)]
inserts

#Upsert to target table
def update_to_sql(df, table_name, key_name):
    a = []
    table = table_name
    primary_key = key_name
    temp_table = f"{table_name}_temporary_table"
    for col in df.columns:
        if col == primary_key:
            continue
        a.append(f'"{col}"=s."{col}"')
    df.to_sql(temp_table, engine, if_exists='replace', index=False)
    update_stmt_1 = f'UPDATE public."{table}" f '
    update_stmt_2 = "SET "
    update_stmt_3 = ", ".join(a)
    update_stmt_4 = f' FROM public."{table}" t '
    update_stmt_5 = f' INNER JOIN (SELECT * FROM public."{temp_table}") AS s ON s."{primary_key}"=t."{primary_key}" '
    update_stmt_6 = f' Where f."{primary_key}"=s."{primary_key}" '
    update_stmt_7 = update_stmt_1 + update_stmt_2 + update_stmt_3 + update_stmt_4 + update_stmt_5 +  update_stmt_6 +";"
    print(update_stmt_7)
    with engine.begin() as cnx:
        cnx.execute(update_stmt_7)

update_to_sql(modified, "stg_IncrementalLoadTest", "CustomerKey")
target = pd.read_sql('Select * from public."stg_IncrementalLoadTest"', engine)
target