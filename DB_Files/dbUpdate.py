#Connect Python with postgress , update data (Assumes table with preloaded data )
import psycopg2

hostname = "localhost"
database = "blockduster"
username = "anju"
pwd = "anju"
port_id = 5432

# to make sure that if the Db connection was not established
# the conn_handle.close and conn.close dont throw error because they 
# have no value
conn = None
conn_handle = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    #open cursor
    conn_handle = conn.cursor()
     
      
    update_statement = """UPDATE customer SET customer_name = %s
                        WHERE customer_id = %s  """
    where_condition = 2
    newValue = "New"
    conn_handle.execute(update_statement,(newValue, where_condition))
    
    count = conn_handle.rowcount
    print(count, "Record updated successfully into mobile table")
    #to save the transaction to be executed.
    conn.commit()
except Exception as error:
    print(error)

#this block will always be excecuted whether exception or not
finally:
    # if the connection is established only then close the
    #cursor and connection.
    if conn_handle is not None:
        conn_handle.close()
    if conn is not None:
        conn.close()
