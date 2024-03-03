import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="bug_tracking_system"
)


def admin_module():
    print("Admin Module")
    while True:
        print("Admin Services")
        print("1. Manage Services (View, Search) ")
        print("2. Manage Employee (Add, View, Search, Edit, Activate/Deactivate) ")
        print("3. Manage Bug( View, Search, AssignBugToExpert) ")
        print("4. Logout")
        break
    choice = input("Enter your choice: ")

    if choice == "1":
        manage_services()
        choice = input("Enter your choice : ")
        if choice == "1":
            view_customers()
        elif choice == "2":
            customer_search_by_name()
        elif choice == "3":
            customer_search_by_login_id()
        else:
            print("Invalid Input! Retry")

    elif choice == "2":
        employee_services()
        choice = input("Enter your choice : ")
        if choice == "4":
            add_new_admin_or_expert()
        elif choice == "5":
            view_all_employees()
        elif choice == "6":
            employee_search_by_name()
        elif choice == "7":
            employee_search_by_login_id()
        elif choice == "8":
            employee_search_by_employee_type()
        elif choice == "9":
            employee_status_update()
        elif choice == "10":
            change_password_admin()
        else:
            print("Invalid Input! Retry")

    elif choice == "3":
        bug_services()
        choice = input("Enter your choice : ")
        if choice == "11":
            view_all_bugs()
        elif choice == "12":
            bug_search_by_bug_id()
        elif choice == "13":
            bug_search_by_bug_status()
        elif choice == "14":
            bug_search_by_customer_login_id()
        elif choice == "15":
            assign_bug_expert()
        elif choice == 16:
            logout()
        else:
            print("Invalid Input! Retry")

    elif choice == "4":
        logout()

    else:
        print("Invalid Input! Retry")


# 1. Manage Services (View, Search)

def manage_services():
    print("Manage Services")
    while True:
        print("1. Customer: View All")
        print("2. Customer: Search - by Customer Name")
        print("3. Customer: Search - by Customer Login Id")
        break


def view_customers():
    print("View all customers here\n")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        # SQL Query to view all customers
        query = "SELECT * FROM  CUSTOMER"
        # Execute the query
        cursor.execute(query)

        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<15s} | {2:<15s} | {3:<8s} | {4:<15s} | {5:<25s}"
        print("------------------------------------------------------------------------------------------------")
        print(s1.format("custLoginId", "custPassword", "custName", "custAge", "custPhone", "custEmail"))
        print("------------------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
        print("------------------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing customer list ", err)


def customer_search_by_name():
    print("Search customer by name here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter customer name :")
        # SQL Query to search customer by name
        query = "SELECT * FROM CUSTOMER WHERE custName = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<15s} | {2:<15s} | {3:<8s} | {4:<15s} | {5:<25s}"
        print("------------------------------------------------------------------------------------------------")
        print(s1.format("custLoginId", "custPassword", "custName", "custAge", "custPhone", "custEmail"))
        print("------------------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
        print("------------------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching customer by name ", err)


def customer_search_by_login_id():
    print("Search customer by Login ID here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter customer Login ID here :")
        # SQL Query to search customer by login ID
        query = "SELECT * FROM CUSTOMER WHERE custLoginId = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<15s} | {2:<15s} | {3:<8s} | {4:<15s} | {5:<25s}"
        print("------------------------------------------------------------------------------------------------")
        print(s1.format("custLoginId", "custPassword", "custName", "custAge", "custPhone", "custEmail"))
        print("------------------------------------------------------------------------------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])))
        print("------------------------------------------------------------------------------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching customer by Login ID ", err)

# 2. Manage Employee (Add, View, Search, Edit, Activate/Deactivate)


def employee_services():
    print("Manage Employee :")
    while True:
        print("4. Employee: Add New (Admin or Expert)")
        print("5. Employee: View All")
        print("6. Employee: Search - by Employee Name")
        print("7. Employee: Search - by Employee Login Id")
        print("8. Employee: Search - by Employee Type")
        print("9. Employee: Activate or Deactivate")
        print("10 .Employee: Change Password")
        break


def add_new_admin_or_expert():
    print("Add new Admin or Expert here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        p = input("Enter Employee Login ID : ")
        q = input("Enter employee password : ")
        r = input("Enter Employee Type : ")
        s = input("Enter Employee Name :")
        t = input("Enter Employee contact no. :")
        u = input("Enter Employee email : ")

        # SQL Query to add new admin or expert
        query = f"INSERT INTO employee(empLoginId ,empPassword, empType, empName, empPhone, empEmail) "\
                f"VALUES('{p}','{q}','{r}','{s}','{t}','{u}')"

        # Execute the query
        cursor.execute(query)
        db.commit()
        print("Employee added successfully")
    except mysql.connector.Error as err:
        print("Error occurred while inserting new employee ", err)


def view_all_employees():
    print("Showing all Employees : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        # SQL Query to view all employee
        query = "SELECT * FROM employee"
        # Execute the query
        cursor.execute(query)
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<25s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while viewing all employee ", err)


def employee_search_by_name():
    print("Search employee by name here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee name :")
        # SQL Query to search employee by name
        query = "SELECT * FROM employee WHERE empName = %s"
        # Execute the query
        cursor.execute(query, (z,))

        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<25s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching employee by name ", err)


def employee_search_by_login_id():
    print("Search employee by Login ID here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee Login ID :")
        # SQL Query to search employee by login ID
        query = "SELECT * FROM employee WHERE empLoginId = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<30s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching employee by Login ID ", err)


def employee_search_by_employee_type():
    print("Search employee by employee type here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee type(ADMIN/EXPERT) :")
        # SQL Query to search employee by employee type
        query = "SELECT * FROM employee WHERE empType = %s"
        # Execute the query
        cursor.execute(query, (z,))
        allrows = cursor.fetchall()

        s1 = "{0:<12s} | {1:<12s} | {2:<10s} | {3:<20s} | {4:<15s} | {5:<30s} | {6:<15s}"
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        print(s1.format("empLoginId", "empPassword", "empType", "empName", "empPhone", "empEmail", "empStatus"))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        for row in allrows:
            print(s1.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])))
        print("-------------------------------------------------------------------------------------------------------"
              "---------------------------")
        cursor.close()
    except mysql.connector.Error as err:
        print("Error occurred while searching employee by type", err)


def employee_status_update():
    print("set employee status here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter updated employee status(ACTIVE/DEACTIVE) :")
        y = input("Enter Employee Name : ")
        # SQL Query to update status of the employee
        query = f"UPDATE employee SET empStatus = '{z}' WHERE empName = '{y}'"
        # Execute the query
        cursor.execute(query)
        db.commit()
        print('Employee Status Updated successfully')
    except mysql.connector.Error as err:
        print("Error occurred while updating status", err)
        db.close()


def change_password_admin():
    print("set new password here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        y = input("Enter Employee Login ID :")
        z = input("Enter new password :")
        # SQL Query to update password
        query = "UPDATE employee SET empPassword = %s WHERE empLoginId = %s "
        # Execute the query
        cursor.execute(query, (z, y))
        db.commit()
        print("Password changed successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating password", err)

#  Bug Services -  Manage Bug( View, Search, AssignBugToExpert )


def bug_services():
    print("Bug Services:")
    while True:
        print("11. Bug: View All")
        print("12. Bug: Search by bugId")
        print("13.Bug: Search by status")
        print("14.Bug: Search by custLoginId")
        print("15.Bug: Assign to Expert")
        print("16.Logout")
        break


def view_all_bugs():
    print("View All Bugs here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        # SQL Query to view all bugs
        query = "SELECT * FROM bug "
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
        print("Error occurred while fetching Bug Table", err)


def bug_search_by_bug_id():
    print("View bug by giving Bug ID here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug ID:")
        # SQL Query to search bug by using bug id
        query = "SELECT * FROM bug WHERE bugId = %s"
        # Execute the query
        cursor.execute(query, (z,))
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
        print("Error occurred while fetching Bug details using Bug ID:", err)


def bug_search_by_bug_status():
    print("View bug by giving Bug Status:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug Status:")
        # SQL Query to search bugs by using status
        query = "SELECT * FROM bug WHERE bugStatus = %s"
        # Execute the query
        cursor.execute(query, (z,))
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
        print("Error occurred while fetching Bug details using Bug Status:", err)


def bug_search_by_customer_login_id():
    print("View bug by giving Customer Login ID:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Customer Login ID:")
        # SQL Query to view bug by using customer login id
        query = "SELECT * FROM bug WHERE custLoginId = %s"
        # Execute the query
        cursor.execute(query, (z,))
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
        print("Error occurred while fetching Bug details using Bug ID ", err)


def assign_bug_expert():
    print("Assigning bug to Expert")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter employee login ID of Expert that you want to assign : ")
        y = input("Enter Bug ID of bug that you want to assign expert to : ")
        # assigning current date and time
        from datetime import datetime
        expertassigneddate = datetime.now()
        # SQL Query to assign bug to expert
        query = f"UPDATE Bug SET expertAssignedDate = '{expertassigneddate}', expertLoginId = '{z}' WHERE bugId = '{y}'"
        # Execute the query
        cursor.execute(query)
        db.commit()
    except mysql.connector.Error as err:
        print("Error occurred while fetching Bug details using Bug ID:", err)


def logout():
    print_login_model()
