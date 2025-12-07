#functions.py

cursor = None
libdb = None

def init(c, db):
    global cursor, libdb
    cursor = c
    libdb = db

def Welcome_Screen():
    status = input("Welcome to our library database, are you a new or returning user?:")
    if status == "new":
        Add_User()
    else:
        Login()

#Login Menu
def Login():
    global current_user
    current_user = None
    print("Login")
    username = input("Username:")
    upassword = input("Password:")

    cursor.execute(
        "SELECT * FROM Users WHERE username = %s and upassword = %s",
        (username, upassword)
    )
    #fetches complete line form db
    name = cursor.fetchone()
    if name:
        current_user = username
        Menu()
    else:
        print("Incorrect user or password")
        Welcome_Screen() 

def Add_User():
    global rflag, lflag, current_user
    username = input("Enter a username: ")
    upassword = input("Enter a password: ")
    ufname = input("Enter your first name: ")
    ulname = input("Enter your last name: ")
    role = input("Enter a role (librarian/reader):")

    if role == "librarian":
        lflag = True
    else:
        rflag = True

    try:
        cursor.execute(
            "INSERT INTO Users (username, upassword, ufname, ulname, rflag, lflag) VALUES (%s, %s, %s, %s, %s, %s)",
            (username, upassword, ufname, ulname, rflag, lflag)
        )
        libdb.commit()
    #Error occurs if a user with the same username already exists
    except:
        print("User already exists.")
        return

    print(f"You are logged in as {username}")
    Menu()

#Deletes a user, logs you out if it is your own account
#Recheck, see how to check which cols added
def Delete_User():
    global current_user
    username = input("Enter the username of the user you would like to delete:")
    cursor.execute(
        "DELETE FROM Users WHERE username = %s",
        (username,)
    )
    libdb.commit()

    print(f"{username} has been deleted.")

    if username == current_user:
        current_user = None
        print("Your account has been deleted.")
        return
    
def Modify_User():
    #If libarian, can alter anyone 
    print("Which user will you be modifying: ")

#Lets the user add a book and its details 
def Add_Book():
    checked_out_by = current_user
    title = input("What is the book title?: ")
    aid = input("What is the author's ID?: ")
    date_published = input("What date was it published? (yyyy-mm-dd): ")
    author = input("Who is the author?: ")

    cursor.execute(
        "INSERT INTO Book(title, aid, date_published, checked_out_by) VALUES (%s, %s, %s, %s)",
        (title, aid, date_published, checked_out_by)
    )
    libdb.commit()

def Delete_Book():
    title = input("Which book would you like to delete?:")
    cursor.execute(
        "DELETE FROM Book WHERE title = %s",
            (title,)
    )
    libdb.commit()

def View_Library():
    cursor.execute("SELECT * FROM Book")
    row = cursor.fetchall()

    print("Current Library:")
    for i in row:
        print(i)

#Finish
def Check_Out_Book():
    global current_user
    checked_book = input("Which book would you like to check out?: ")

    cursor.execute("SELECT checked_out_by FROM Book WHERE title = %s",
        (checked_book,)
    )
    exists = cursor.fetchone()

    if not exists:
        print("That book is not in the library.")
        return

    check_out_date = input("What is the date? (yyyy-mm-dd): ")

    cursor.execute("UPDATE Book SET checked_out_by = %s, check_out_date = %s WHERE title = %s",
                   (current_user, check_out_date, checked_book)
    )
    libdb.commit()

#Finish, if book not checked out, give error message
def Return_Book():
    global current_user
    returned_book = input("Which book are you returning?: ")

    cursor.execute(
        "SELECT checked_out_by FROM Book WHERE title = %s",
        (returned_book,)
    )

    row = cursor.fetchone()
    if not row or row[0] != current_user:
        print("Error: Book isn't available for return")
        #Menu()
        #return
    
    cursor.execute(
        "UPDATE Book SET checked_out_by = NULL, check_out_date = NULL WHERE title = %s",
        (returned_book,)
    )
    libdb.commit()


def Avg_Time_Checked_out():
    print("hi")

#Choice menu
def Menu():
    while True:
        print("Welcome to the library!")
        print("1. Delete a User")
        print("2. Add a Book")
        print("3. Delete a Book")
        print("4. View Library")
        print("5. Check Out a Book")
        print("6. Return a Book")
        print("7. Modify a User")
        choice = input("Choose an option:")
        match choice:
            case "1":
                Delete_User()
            case "2":
                Add_Book()
            case "3":
                Delete_Book()
            case "4":
                View_Library()
            case "5":
                Check_Out_Book()
            case "6":
                Return_Book()
            case "7":
                Modify_User()


