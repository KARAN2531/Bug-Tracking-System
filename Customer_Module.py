# CUSTOMER MODULE

import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="bug_tracking_system "
)


def customer_module():
    print("Customer Module : ")
    while True:
        print("1) Create Account")
        print("2) Update Account")
        print("3) Post New Bug")
        print("4) View All Bugs")
        print("5) Search Bugs based on status")
        print("6) View Bug Solution")
        print("7) Change Password")
        break

    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        list_update_account()
        choice = input("Enter your choice: ")
        if choice == "1":
            update_login_id()
        elif choice == '2':
            update_name()
        elif choice == "3":
            update_age()
        elif choice == "4":
            update_contact_number()
        elif choice == "5":
            update_email()
        else:
            print("Invalid Input. Retry! ")
    elif choice == "3":
        post_new_bug()
    elif choice == "4":
        view_all_bugs_customer()
    elif choice == "5":
        bug_search_by_bug_status_customer()
    elif choice == "6":
        view_bug_solution()
    elif choice == "7":
        change_password()
    else:
        logout()


def create_account():
    print("Creating new account:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        p = input("Enter Customer Login ID : ")
        q = input("Enter Customer password : ")
        r = input("Enter Customer Name : ")
        s = input("Enter Customer Age : ")
        t = input("Enter Customer contact no. :")
        u = input("Enter Customer email : ")

        # SQL Query to add new customer
        query = f"INSERT INTO customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail)" \
                f"VALUES('{p}', '{q}', '{r}', '{s}', '{t}', '{u}')"
        # Execute the query
        cursor.execute(query)
        db.commit()
        print("Account created Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while creating new account. ", err)


def list_update_account():
    print("Select Option to Update : ")
    while True:
        print("1. Customer Login ID")
        print("2. Customer Name")
        print("3. Customer Age")
        print("4. Customer Contact Number")
        print("5. Customer Email")
        break


def update_login_id():
    print("Update Login ID here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter old Customer Login ID : ")
        z = input("Enter new customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custLoginId = '{z}' WHERE custLoginId = '{y}' AND password = '{x}'"
        # Execute the query
        cursor.execute(query)
        print("Login Id Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating customer Login ID. ", err)


def update_name():
    print("Update name here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new name here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custName = '{y}' WHERE custLoginId = '{z}' AND password = '{x}'"
        # Execute the query
        cursor.execute(query)
        print("Name Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating name. ", err)


def update_age():
    print("Update Age here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new Age here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custAge = '{y}' WHERE custLoginId = '{z}' AND password = '{x}'"
        # Execute the query
        cursor.execute(query)
        print("Age Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating Age. ", err)


def update_contact_number():
    print("Update contact number here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new contact number here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custPhone = '{y}' WHERE custLoginId = '{z}' AND password = '{x}' "
        # Execute the query
        cursor.execute(query)
        print("Contact Number Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating contact number. ", err)


def update_email():
    print("Update email here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter your password here : ")
        y = input("Enter new email here : ")
        z = input("Enter customer Login ID :")
        # SQL Query to search customer by login ID
        query = f"UPDATE customer SET custEmail = '{y}' WHERE custLoginId = '{z}' AND password = '{x}' "
        # Execute the query
        cursor.execute(query)
        print("Email Id Updated Successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating email. ", err)


def post_new_bug():
    print("Post new bug here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        cust_login_id = input("Enter your login ID: ")
        product_name = input("Enter the product name: ")
        bug_desc = input("Enter the bug description: ")
        from datetime import datetime
        bugpostingdate = datetime.now()
        query = f"INSERT INTO bug(bugPostingDate = '{bugpostingdate}', custLoginId = '{cust_login_id}, " \
                f"productName = '{product_name}', bugDesc = '{bug_desc})' "
        cursor.execute(query)
        db.commit()
        print("Bug posted successfully!")
    except mysql.connector.Error as err:
        print("Error occurred while posting new bug. ", err)


def view_all_bugs_customer():
    print("View all Bugs here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter Customer Login ID : ")
        # SQL Query to view all Bugs of customer itself
        query = f"SELECT * FROM  bug WHERE custLoginId = '{x}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing bugs. ", err)


def bug_search_by_bug_status_customer():
    print("View bug by giving Bug Status here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug Status:")
        x = input("Enter Customer Login ID : ")
        # SQL Query to search bugs by using status
        query = f"SELECT * FROM bug WHERE bugStatus = '{z}' AND custLoginId = '{x}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching Bug details using Bug Status. ", err)


def view_bug_solution():
    print("View solution of bugs here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter BUG ID : ")
        y = input("Enter your customer login Id : ")
        # SQL Query to view bug solution
        query = f"SELECT * FROM bug WHERE bugId = '{x}' AND custLoginId = '{y}' "
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<8s} | {1:<20s} | {2:<12s} | {3:<10s} | {4:<12s} | {5:<30s} | {6:<20s} | {7:<16s} | " \
             "{8:<16s} | {9:<30s}"
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        print(s1.format("bugId", "bugPostingDate", "custLoginId", "bugStatus", "productName", "bugDesc",
                        "expertAssignedDate", "expertLoginId", "bugSolvedDate", "solution"))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),
                            str(row[6]), str(row[7]), str(row[8]), str([9])))
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing Bug Solution. ", err)


def change_password():
    print("set new password here :")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter Current password")
        y = input("Enter Customer Login ID")
        z = input("Enter new password :")
        # SQL Query to update password
        query = f"UPDATE customer SET custPassword = '{z}' WHERE custLoginId = '{y}' AND custPassword = '{x}' "
        # Execute the query
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Error occurred while updating password. ", err)
