#Connecting Python with Postgress 
#Create table and insert data
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
    #multi line statement with three quotes
    
    create_script = '''CREATE TABLE if NOT EXISTS customer 
                        (customer_id SERIAL PRIMARY KEY,
                         customer_name VARCHAR(100) NOT NULL,
                         customer_address VARCHAR(200), 
                         customer_city VARCHAR(60),
                         customer_state VARCHAR(60),
                         customer_phone VARCHAR(100) ) '''
    #to run the script
    cur.execute(create_script)
    
    insert_script = '''INSERT INTO customer 
                        (customer_name, customer_address,
                         customer_city, customer_state,
                         customer_phone) 
    VALUES(%s,%s,%s,%s,%s) '''
    insert_values = ("Joseph", "67 Canal lane", "Paramus" ,"NJ","1113332222")
    cur.execute(insert_script, insert_values)
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
