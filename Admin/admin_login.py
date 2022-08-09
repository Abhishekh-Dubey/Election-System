import mysql.connector
def admin_login():
    uname=input("Enter your username : ")
    pwd=input("Enter your password : ")
    return uname,pwd
def connect_db(u,p):
    db=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="election")
    mycursor=db.cursor()
    mycursor.execute(f"select Name from admin where User_name='{u}' and Password='{p}'")
    acc=mycursor.fetchone()

    if acc:
        print("*" * 60)
        print("Login sucessfull".center(60))
        from Admin import admin_options
        admin_options.flow_admin(acc)
    else:
        print("Check your Credientials")
def admin_main():
    u,p=admin_login()
    connect_db(u,p)

#admin_main()

