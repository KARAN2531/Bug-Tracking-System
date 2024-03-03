import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="bug_tracking_system ")


def print_login_model():
    print("Please select Your Role ")
    while True:
        print(" 1) Login as Admin")
        print(" 2) Login as Expert")
        print(" 3) Login as Customer")
        break


def admin_login():
    username = input("Enter Admin Login ID : ")
    userpassword = input("Enter Admin Password : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    # sql query to check password
    query = " select * from employee where username = '%s' "
    values = username
    cursor.execute(query % values)
    try:
        row = cursor.fetchmany(1)[0]
        dbPass = row[1]
        if userpassword == dbPass:
            print("Login authentication success")
            utype = row[2]
            if utype == 'ADMIN':
                admin_module()
            else:
                expert_module()
        else:
            print("Login authentication failed")
    except IndexError:
        print("Invalid User Name or password .Retry...")

    db.commit()
    db.close()


def customer_login():
    username = input("Enter customer Login ID : ")
    userpassword = input("Enter customer Password : ")
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    # sql query to check password
    query = " select * from customer where custLoginId = '%s' "
    values = username
    cursor.execute(query % values)
    try:
        row = cursor.fetchmany(1)
        dbPass = row[1]
        if userpassword == dbPass:
            print("Login authentication success")
            customer_module()
        else:
            print("Login authentication failed")
    except IndexError:
        print("Invalid User Name or password  .Retry...")

    db.commit()
    db.close()
