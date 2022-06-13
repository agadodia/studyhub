#Connect Python to postgress dalete a row (Assumes data in table)
import psycopg2

hostname = "localhost"
database = "blockduster"
username = "anju"
pwd = "anju"
port_id = 5432

# to make sure that if the Db connection was not established
# the cur.close and conn.close dont throw error because they 
# have no value
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    #open cursor
    cur = conn.cursor()
        
    delete_query = """DELETE FROM customer where customer_id = 5 """
    cur.execute(delete_query)
    whereCondition = 6
    #cur.execute(delete_query, (whereCondition))
    count = cur.rowcount
    print(count, "Record deleted from customer.")
    
   
    #to save the transaction to be executed.
    conn.commit()
    
except Exception as error:
    print(error)

#this block will always be excecuted whether exception or not
finally:
    # if the connection is established only then close the
    #cursor and connection.
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
