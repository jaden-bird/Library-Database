import mysql.connector

#libdb = mysql.connector.connect(
#    host="localhost",
#    user="root",
 #   password="..."
#)

#cursor = libdb.cursor()

### PSEUDOCODE
#user class??

Add_User():
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