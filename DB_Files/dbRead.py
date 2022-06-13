# Python reading from postgress db
# Dictionary reading format also shown
import psycopg2
import psycopg2.extras

hostname = "localhost"
database = "blockduster"
username = "anju"
pwd = "anju"
port_id = 5432

# to make sure that if the Db connection was not established
# the conn_handle.close and conn.close dont throw error because they 
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
    #open conn_handle
    conn_handle = conn.cursor()
        
    # reading records from customers
    conn_handle.execute("SELECT * FROM customer")
    records = conn_handle.fetchall()
    for record in records :
        print(record)
    for record in records :
        print(record[0],record [1], record[2], record[3])
    # Printing in the dictionary format for easy access 
    # as key value pair using psycopg2.extra.DictCursor
    conn_handle2 = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

    conn_handle2.execute("SELECT * FROM customer")
    formatedRecords = conn_handle2.fetchall()
    #print using key value pair
    for formatedRecord in formatedRecords :
        print(formatedRecord["customer_id"],formatedRecord ["customer_name"], formatedRecord["customer_address"], formatedRecord["customer_city"])
    
    #to save the transaction to be executed.
    conn.commit()
    
except Exception as error:
    print(error)

#this block will always be excecuted whether exception or not
finally:
    # if the connection is established only then close the
    #conn_handle and connection.
    if conn_handle is not None:
        conn_handle.close()
    if conn is not None:
        conn.close()
