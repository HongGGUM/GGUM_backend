import mysql.connector

#MySQL �������� ����
app.config['MYSQL_HOST'] = 'honggumdb.capnwelofgc3.ap-northeast-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'hongik45'
app.config['MYSQL_DB'] = 'honggumdb'

#MySQL ���� ����
def get_connection():
	conncection = mysql.connector.connect(
		host=app.config['MYSQL_HOST'],
		user=app.config['MYSQL_USER'],
		password=app.config['MYSQL_PASSWORD'],
		database=app.config['MYSQL_DB'],
		)
	return connection