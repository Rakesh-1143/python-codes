import cx_Oracle
con=cx_Oracle.connect("system/tiger@127.0.0.1/orcl")
print("type of kvr variable",type(con))
print("python program sucessfully connected with data base")
cur=con.cursor()
print("Type of cur variable=",type(cur))
print("cursor is sucessfully connected")
