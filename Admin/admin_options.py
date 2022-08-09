import sys
def admin_option(acc):
    print("*" * 60)
    print(f"WELCOME {acc[0].upper()} TO ADMIN PAGE".center(60))
    print("*" * 60)
    print("1.Voter Registration\n2.Candidate Registration\n3.View Candidates\n4.Session Time\n5.show Results\n6.Logout\n7.Exit")
    ch=int(input("-------Enter your choice---------: "))
    return ch
def flow_admin(acc):
    ch=admin_option(acc)
    if ch==1:
        from Voter import voter_regis_page
        voter_regis_page.sql_connect(acc)
    elif ch==2:
        from candidate import candy_regis_page
        candy_regis_page.main_connect(acc)
    elif ch==3:
        from Voter import view_candidate_details
        view_candidate_details.show_area_candy(acc)

    elif ch==4:
        from Admin import session_time
        session_time.time(acc)
    elif ch==5:
        from Admin import show_results
        show_results.show_main(acc)
    elif ch==6:
        import start_page
        start_page.flow()
    elif ch==7:
        sys.exit(0)

    else:
        print("*" * 50)
        print("Give Correct Choice".center(45))
        print("*" * 50)
        import start_page
        start_page.flow()

