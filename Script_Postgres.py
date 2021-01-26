import ac_tools
import m245
# make sure that all connections are closed
ac_tools.close_connections(globals())
# create the user table and load the user_accounts.csv file into it
m245.create_and_fill_users_table("dbname=dq user=dq")
##INITIAL CODE ENDS
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
users = cur.fetchall()
conn.close()
