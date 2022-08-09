import mysql.connector

def show_main(acc):
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
    for i in l:
        print(j,i)
        j = j + 1

    for k in range(2):
        print("*" * 60)
        x = (input("Type Your Area from given option: ")).upper()
        print("*" * 60)
        if x not in l:
            print("-" * 60)
            print("please see from upper options")
            print("-" * 60)
        else:
            mycursor.execute(f"select Name from candidate where Area='{x}' ORDER BY voter_contt	 DESC LIMIT 1")
            acc2 = mycursor.fetchone()
            for j in acc2:
                print("*" * 60)
                print(f"Winner From This Area is: {j}".center(60))
                print("*" * 60)
            from extra_file import exit_code
            exit_code.exit_main(acc)
    print("*" * 60)
    print("you are tried much time")
    print("pleas LOGIN AGAIN  !!!!")
    print("*" * 60)
    import start_page
    start_page.flow()
#show_main(100)