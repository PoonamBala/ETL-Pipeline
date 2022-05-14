-- Use AWS RDS MySQL database: business

-- Drop Table business.table1
CREATE TABLE business.table1 (
  `id` int NOT NULL,
  `foriegnkey1_id` varchar(32) NOT NULL,
  `datetime1` timestamp NULL DEFAULT NULL,
  `datetime2` timestamp NULL DEFAULT NULL,
  `status` varchar(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL
)

-- Truncate Table business.table1
INSERT INTO business.table1 VALUES
	  (1,'b68212901','2021-04-25 07:31:15','2021-04-25 07:31:15','status01','name01','description01')
	 ,(2,'b48462028','2021-04-25 07:31:15','2021-04-25 07:31:15','status02','name02','description02')
	 ,(3,'b92347849','2021-04-25 07:31:15','2021-04-25 07:31:15','status03','name03','description03')
	 ,(4,'b38395000','2021-04-25 07:31:15','2021-04-25 07:31:15','status04','name04','description04')
	 ,(5,'b24903742','2021-04-25 07:31:15','2021-04-25 07:31:15','status05','name05','description05')
	 ,(6,'b37594939','2021-04-26 07:31:15','2021-04-26 07:31:15','status06','name06','description06')
	 ,(7,'b85739950','2021-04-26 07:31:15','2021-04-26 07:31:15','status07','name07','description07')
	 ,(8,'b84859066','2021-04-26 07:31:15','2021-04-26 07:31:15','status08','name08','description08')
	 ,(9,'b94050506','2021-04-26 07:31:15','2021-04-26 07:31:15','status09','name09','description09')
	,(10,'b00603494','2021-04-26 07:31:15','2021-04-26 07:31:15','status10','name10','description10')
	;

Select
	id
	,foriegnkey1_id
	,datetime1
	,datetime2
	,status
	,name
	,description
FROM
	table1
Limit 100
