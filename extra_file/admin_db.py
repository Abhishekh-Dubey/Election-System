import mysql.connector

def add_data():
    db = mysql.connector.connect(host="localhost", port="3306", user="root", password="")
    mycursor = db.cursor()
    mycursor.execute(f"CREATE DATABASE if not exists election1 ")

    db=mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='election1')
    mycursor=db.cursor()
    mycursor.execute("CREATE TABLE if not exists admin(Admin_id int PRIMARY KEY AUTO_INCREMENT, Name varchar(50),User_name varchar(50),Password varchar(50))")
    incre="ALTER TABLE admin AUTO_INCREMENT =100"
    mycursor.execute(incre)

    mycursor.execute(f"insert into admin(Name,User_name,Password) values ('Abhishekh Dubey','abhi123','abhi123')")
    db.commit()

    mycursor.execute("CREATE TABLE if not exists voter(voter_id int PRIMARY KEY AUTO_INCREMENT, Name varchar(50),Address varchar(50),Password varchar(50),voter_count int)")
    incre = "ALTER TABLE voter AUTO_INCREMENT =1000"
    mycursor.execute(incre)
    db.commit()

    mycursor.execute("CREATE TABLE if not exists candidate(candidate_id int PRIMARY KEY AUTO_INCREMENT,Name varchar(50),Area varchar(50),Party varchar(50),voter_contt int)")
    incre = "ALTER TABLE candidate AUTO_INCREMENT =500"
    mycursor.execute(incre)
    db.commit()

    mycursor.execute("CREATE TABLE if not exists time_table(Area varchar(50) PRIMARY KEY,Start_time TIME,End_time TIME)")
    db.commit()

add_data()


