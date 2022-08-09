import datetime
import mysql.connector

def time(acc):
    db = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="election")
    mycursor = db.cursor()
    mycursor.execute(f"select distinct Area  from candidate ")
    result = mycursor.fetchall()
    l = []
    for i in result:
        l.append(i[0])
    print("^" * 60)
    print(("Select Your Area ").center(60))
    print("^" * 60)
    j = 1
    for i in result:
        print(j, i[0])
        j = j + 1
    for k in range(2):

        print("*" * 60)
        x=(input("Type Your Area from given option: ")).upper()
        print("*" * 60)
        if x not in l:
            print("-" * 60)
            print("please see from upper options")
            print("-" * 60)
        else:
            mycursor.execute(f"select Start_time,End_time from time_table where Area='{x}'")
            mycursor.fetchall()
            #start
            t=input("Enter your start_time (h:m:s): ")
            #end
            p=input("Enter your End_time (h:m:s): ")
            str_s=datetime.datetime.strptime(t,"%H:%M:%S")
            str_e = datetime.datetime.strptime(p,"%H:%M:%S")
            str_st=(str_s.time())
            str_ed=(str_e.time())
            print("-" * 60)
            print(f'Start time is: {str_st} and End time is: {str_ed}')
            print("-" * 60)
            sql_s=f"update time_table set Start_time='{str_st}' where Area='{x}'"
            sql_e = f"update time_table set End_time='{str_ed}' where Area='{x}'"
            mycursor.execute(sql_s)
            mycursor.execute(sql_e)
            db.commit()
            from extra_file import exit_code
            exit_code.exit_main(acc)
    print("*" * 60)
    print("you are tried much time")
    print("pleas LOGIN AGAIN  !!!!")
    print("*" * 60)
    import start_page
    start_page.flow()
#time(100)