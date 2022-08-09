import mysql.connector
def view_db_candidate():
        db = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="election")
        mycursor = db.cursor()
        mycursor.execute('select * from candidate')
        result=mycursor.fetchall()
        for i in result:
                print(i)
