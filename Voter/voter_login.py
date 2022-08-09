import mysql.connector
from datetime import datetime
from datetime import timedelta
def voter_login():
    uname=input("Enter your voter id : ")
    pwd=input("Enter your password : ")
    return uname,pwd
def voter_connect_db(uname,pwd):
    current_time = datetime.now()
    cur_time = current_time.strftime("%H:%M:%S")
    db=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="election")
    mycursor=db.cursor()
    mycursor.execute(f"select voter_id,Name,Address,voter_count from voter where voter_id='{uname}' and Password='{pwd}'")
    acc = mycursor.fetchone()
    d=acc[2]
    s=d.upper()
    print("-" * 60)
    print(f"Area Name is: {s}".center(60))
    print("-" * 60)
    mycursor.execute(f"select Start_time,End_time from time_table where area='{s}'".center(60))
    acc1=mycursor.fetchall()
    k=str(acc1[0][0])
    d=str(acc1[0][1])


    if cur_time<k:
        print("-" * 60)
        print(f"Voting will start at:- {k}".center(55))
        print("-" * 60)
        print("1.Logout\n2.Exit\n")
        ch = int(input("--------Enter Your Choice-------:"))
        if ch == 1:
            import start_page
            start_page.flow()
        elif ch == 2:
            sys.exit(0)
        else:
            print("correct option")

    elif cur_time>=k:
        if cur_time>=d:
            print("*" * 60)
            print("voting time is over".center(60))
            print("*" * 60)
            print(f"Result Displayed From Area:  {s}".center(60))
            print("*" * 60)
            mycursor = db.cursor()
            mycursor.execute(f"select Name from candidate where Area='{s}' ORDER BY voter_contt DESC LIMIT 1")
            acc2 = mycursor.fetchall()
            g=acc2[0][0]
            print(f'Winner Candidate Name is: {g}'.center(55))
            print("*" * 60)
        elif cur_time<d:
            if acc[3]>=1:
                print("-" * 60)
                print('You Already Voted.....Thank You'.center(60))
                print("*" * 60)
                print("WINNER FROM THIS AREA IS: ".center(60))
                print("*" * 60)

            else:
                mycursor.execute(f"select candidate_id,Name,Area from candidate where Area='{acc[2]}'")
                acc1=mycursor.fetchall()
                l=[]
                for i in acc1:
                    l.append(i[0])
                print("*" * 50)
                print((f"Login sucessfull....You belongs to Area:  {acc[2]}").center(60))
                print("*" * 50)
                print((f"Welcome {acc[1]}").center(45))
                print("*" * 50)

                for i in acc1:
                    print(i[0],i[1],i[2])
                for i in range(2):
                    print("-" * 60)
                    x=(int(input("Please Enter Candidate Id to whome you want to vote: ".center(55))))
                    print("-" * 60)

                    if x not in l:
                        print("please see from upper options")
                    else:
                        mycursor.execute(f"update candidate set voter_contt=voter_contt+1 where candidate_id={x}")
                        db.commit()
                        mycursor.execute(f"update voter set voter_count=voter_count+1 where voter_id={acc[0]}")
                        print("*" * 60)
                        print("Thank you for your auspicious Time and Vote".center(60))
                        print("*" * 60)
                        db.commit()
                        import start_page
                        start_page.flow()
def voter_main():
    uname,pwd=voter_login()
    voter_connect_db(uname,pwd)
#voter_main()

