import mysql.connector

def voter_input():
    name=input("Enter Voter name: ")
    add=input("Enter Voter address: ")
    pwd=input("Enter Voter password: ")
    return name,add,pwd

def sql_connect(acc):
    name,add,pwd=voter_input()
    db=mysql.connector.Connect(host="localhost",port="3306",user="root",password="",database="election")
    mycursor=db.cursor()
    z=(f"insert into voter(Name,Address,Password,voter_count) values ('{name}','{add}','{pwd}','{0}')")
    mycursor.execute(z)
    db.commit()
    print("*" * 60)
    print("Voter Registration Done Successfully...Thank You".center(60))
    print("*" * 60)
    from extra_file import exit_code
    exit_code.exit_main(acc)
#sql_connect()
