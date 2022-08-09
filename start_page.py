import sys
def main_page():
    print("1. Admin Login\n2. Voter Login\n3. Exit\n")
    ch = int(input("-------- Enter your choice --------: "))
    return ch

def flow():
    for i in range(2):
        ch = main_page()
        if ch==1:
            from Admin import admin_login
            admin_login.admin_main()
        elif ch==2:
            from Voter import voter_login
            voter_login.voter_main()
        elif ch==3:
            sys.exit(0)
        else:
            print("check your secure credentials")
flow()

