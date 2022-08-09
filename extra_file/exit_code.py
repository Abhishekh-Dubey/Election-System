import sys
def exit_main(acc):

    print("1.Back to menu\n2.Logout\n3.Exit")
    ch = int(input("------Enter Your Choice------> "))
    if ch == 1:
        from Admin import admin_options
        admin_options.flow_admin(acc)
    elif ch == 2:
        import start_page
        start_page.flow()
    elif ch == 3:
        sys.exit(0)
    else:
        print("invalid choice")
