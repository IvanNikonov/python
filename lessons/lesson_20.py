import psycopg2

connection = psycopg2.connect("host=PostgreSQL-16 dbname=learning user=learning password=tester")
cursor = connection.cursor()
result = cursor.execute("SELECT * FROM goods")
print(cursor.fetchall())