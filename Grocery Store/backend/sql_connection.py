import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx == None:
        __cnx = mysql.connector.connect(user='root', password='',
                                          host='localhost',
                                          database='grocery_store')
    return __cnx
