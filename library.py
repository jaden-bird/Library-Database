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

#Lets user add an account, the specifics will be inserted
#into the User table 
def Welcome_Screen():
    status = input("Welcome to our library database, are you a new or returning user?:")
    if status == "new":
        Add_User()
    else:
        Login()

def Add_User():
    global rflag, lflag
    username = input("Enter a username:")
    upassword = input("Enter a password:")
    ufname, ulname = input("What is your first and last name?").split()
    role = input("Enter a role (librarian/reader):")
    if role == "librarian":
        lflag = True
    else:
        rflag = True

    try:
        cursor.execute(
            "INSERT INTO Users (username, upassword, rflag, lflag, ufname, ulname) VALUES (%s, %s, %s, %s, %s, %s)",
            (username, upassword, rflag, lflag, ufname, ulname)
        )
        libdb.commit()
    #Error occurs if a user with the same username already exists
    except mysql.connector.errors.IntegrityError:
        print("User already exists.")

def Login():
    username = input("Username:")
    upassword = input("Password:")

    cursor.execute(
        "SELECT * FROM Users WHERE username = %s and upassword = %s",
        (username, upassword)
    )
    #fetches complete line form db
    name = cursor.fetchone()
    if name:
        print("Welcome back")
        #Menu()
    else:
        print("Incorrect user or password")
        Welcome_Screen()  

Welcome_Screen()


### PSEUDOCODE
#user class??

''' Add_User():
    input("what type of user? (lib or reader)")
    input("Username:")
    input("password:")

Login()
    input ("user and pass")
    check if user is in db
    if pass.user == user.user 
        let in
    else    
        prompt again

Delete_User()
    if (lib == true)
        del chosen user 
    if (user_acct == user_acct_del)
        del chosen user 

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


Menu()
    choose an action & calls the function
        '''