import mysql.connector

#libdb = mysql.connector.connect(
#    host="localhost",
#    user="root",
 #   password="..."
#)

#cursor = libdb.cursor()
Rflag = False
Lflag = False

#Lets user add an account, the specifics will be inserted
#into the User table 
def Add_User(Rflag, Lflag):
    username = input("Enter a username:")
    pword = input("Enter a password:")
    role = input("Enter a role (librarian/reader):")
    if role == "librarian":
        Lflag = True
    else:
        Rflag = True

    try:
        cursor.execute(
            "INSERT INTO Users (username, pword, Rflag, Lflag)"
            (username, pword, Rflag, Lflag)
        )
        conn.commit()
    #Error occurs if a user with the same username already exists
    except mysql.connector.errors.IntegrityError:
        print("User already exists. Try another.")

def Login():
    username = input("Username:")
    password = input("Password:")


status = input("Welcome to our library database, are you a new or rerning user?:")
if status == "new":
    Add_User()
else:
    Login()


### PSEUDOCODE
#user class??

''' Add_User():
    input("what type of user? (lib or reader)")
    input("Username:")
    input("password:")

Login()
    input ("user and pass")
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
        '''