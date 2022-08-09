import mysql.connector

def candidate_input():
    name=input("Enter Candidate name: ")
    area=input("Enter Candidate area: ")
    party=input("Enter Candidate party: ")
    return name,area,party

def candy_db_connect(name,area,party):
    db=mysql.connector.Connect(host="localhost",port="3306",user="root",password="",database="election")
    mycursor=db.cursor()
    a=(f"insert into candidate(Name,Area,Party,voter_contt) values ('{name}','{area}','{party}','{0}')")
    mycursor.execute(a)
    db.commit()
def main_connect(acc):
    name,area,party=candidate_input()
    candy_db_connect(name,area,party)
    print("*" * 60)
    print(("Candidate Registration Done Successfully...Thank You").center(60))
    print("*" * 60)
    from extra_file import exit_code
    exit_code.exit_main(acc)
