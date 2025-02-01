import cx_Oracle
try:
    con = cx_Oracle.connect("system/tiger@127.0.0.1/orcl")
    print("Type of con variable:", type(con))
    print("Python program successfully connected with the database")
    cur = con.cursor()
    print("Type of cur variable:", type(cur))
    print("Cursor is successfully connected")

except cx_Oracle.DatabaseError as e:
    print("There was a problem connecting to Oracle:", e)

finally:
    # Closing the connection
    if 'cur' in locals():
        cur.close()
    if 'con' in locals():
        con.close()

