import mysql.connector

libdb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="libpassword!",
    database = "library"
)

cursor = libdb.cursor()
rflag = False
lflag = False
 
def Welcome_Screen():
    status = input("Welcome to our library database, are you a new or returning user?:")
    if status == "new":
        Add_User()
    else:
        Login()

#Lets user add an account, the specifics will be inserted
#into the User table

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

#Lets the user add a book and its details 
def Add_Book():
    checked_out_by = current_user
    title = input("What is the book title?: ")
    aid = input("What is the author's ID?: ")
    date_published = input("What date was it published? ('yyyy-mm-dd'): ")
    check_out_date = input("What is the date? ('yyyy-mm-dd'): ")
    author = input("Who is the author?: ")

    cursor.execute(
        "INSERT INTO Book(title, aid, date_published, checked_out_by, check_out_date) VALUES (%s, %s, %s, %s, %s)",
        (title, aid, date_published, checked_out_by, check_out_date)
    )
    libdb.commit()

def Delete_Book():
    title = input("Which book would you like to delete?:")
    cursor.execute(
        "DELETE FROM Book WHERE title = %s",
            (title,)
    )
    libdb.commit()

#Choice menu
def Menu():
    while True:
        print("Welcome to the library!")
        print("1. Delete a User")
        print("2. Add a Book")
        print("3. Delete a Book")
        choice = input("Choose an option:")
        match choice:
            case "1":
                Delete_User()
            case "2":
                Add_Book()
            case "3":
                Delete_Book()
            #case "4":
                #Show_Book_Selection()
           #case "5":
                #Check_Out_Book()
            #case "6":
                #Return_Book()
            #case "7":
                #Modify_User

def Add_User():
    global rflag, lflag
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
    except mysql.connector.errors.IntegrityError:
        print("User already exists.")
        return

    print(f"You are logged in as {username}")
    Menu()

Welcome_Screen() 

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
        return


### PSEUDOCODE
#user class??

'''
Add_book()
    if (lib == true)
        add books, publisher, author
        to respective tables

Delete_book()
    if (lib == true)
        delete books (and all info connected)

Check_out_book()
    if(check if book is NUll in checked out)
        update checked_out to True
        update checked_out to current_date

Return_book()
    if (book is not NULL )
        update checked_out to False
        check_in_date update (?)
                              
Modify_user()
    if (librarian == true or user_acct == act_user)
        update user attributes

Search/View books

        '''