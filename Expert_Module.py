import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="bug_tracking_system "
)


# EXPERT MODULE


def expert_module():
    print("Expert Module : ")
    while True:
        print("1) View Assigned Bug")
        print("2) Filter Assigned Bugs based on status")
        print("3) Solve the Bug")
        print("4) Change Password")
        break
    choice = input("Enter your choice:")

    if choice == "1":
        view_assigned_bug()
    elif choice == "2":
        filter_assigned_bugs_based_on_status()
    elif choice == "3":
        solve_the_bug()
    elif choice == "4":
        change_password_expert()
    else:
        print("Invalid Input. Retry...")


def view_assigned_bug():
    print("View assigned bug here : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Expert ID:")
        # SQL Query to search assigned bugs
        query = f"SELECT * FROM bug WHERE expertLoginId = '{z}' "
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
        print("Error occurred while fetching Assigned Bug details. ", err)


def filter_assigned_bugs_based_on_status():
    print("View assigned bugs based on Bug Status:")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Bug Status:")
        x = input("Enter Expert Login ID : ")
        # SQL Query to search bugs by using status
        query = f"SELECT * FROM bug WHERE bugStatus = '{z}' AND expertLoginId = '{x}' "
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
        print("Error occurred while fetching Bug details using Bug Status.", err)


def solve_the_bug():
    print("Solve Bugs here ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        z = input("Enter Solution : ")
        x = input("Enter Bug ID : ")
        # assigning current date and time
        from datetime import datetime
        bugsolvedate = datetime.now()
        # SQL Query to search bugs by using status
        query = f"UPDATE Bug SET solution = '{z}', bugSolvedDate = '{bugsolvedate}' WHERE bugId = '{x}' "
        # Execute the query
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("Error occurred while Updating Bug Solution.", err)


def change_password_expert():
    print("set new password here")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    try:
        x = input("Enter Old password : ")
        y = input("Enter Expert Login ID : ")
        z = input("Enter new password : ")
        # SQL Query to update password
        query = f"UPDATE employee SET empPassword = '{z}' WHERE empLoginId = '{y}' AND empPassword = '{x}' "
        # Execute the query
        cursor.execute(query)
        print("Password changed successfully")
    except mysql.connector.Error as err:
        print("Error occurred while updating password:", err)
