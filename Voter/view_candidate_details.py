import mysql.connector

def show_area_candy(acc):

    db = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="election")
    mycursor = db.cursor()
    mycursor.execute(f"select distinct Area  from candidate ")
    result = mycursor.fetchall()
    l = []
    for i in result:
        l.append(i[0])
    print("^" * 50)
    print(("Select Your Area ").center(45))
    print("^" * 50)
    j=1
    for i in l:
        print(j,i)
        j=j+1
    for k in range(2):
        x = (input("Enter your area name: ")).upper()
        if x not in l:
            print("-" * 60)
            print("please see from upper options")
            print("-" * 60)
        else:
            print("*"*60)
            print("CANDIDATE_IT\tNAME\t\tPARTY\t\tTOTEL VOTE")
            print("*" * 60)
            mycursor.execute(f"select candidate_id,Name,Party,voter_contt from candidate where Area='{x}'")
            result=mycursor.fetchall()
            for i in result:
                print(f"\t{i[0]}\t\t\t{i[1]}\t\t{i[2]}\t\t\t\t{i[3]}")
            from extra_file import exit_code
            exit_code.exit_main(acc)
    print("*" * 60)
    print("you are tried much time")
    print("pleas LOGIN AGAIN  !!!!")
    print("*" * 60)
    import start_page
    start_page.flow()
#show_area_candy(100)