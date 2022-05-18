import sqlite3
conn = sqlite3.connect('Database/Userdata.db')
cursor = conn.cursor()

# create table
q = ''' CREATE TABLE IF NOT EXISTS User(
    Name TEXT (20) NOT NULL,
    Username TEXT (20) NOT NULL,
    password TEXT (10) NOT NULL,
    mobile number (10) NOT NULL
   )'''
cursor.execute(q)
print("table created")
def login():
    un=input("enter your username")
    p=input("enter your password")
    q='''select * from User 
    where Username=? and password=?'''
    userdata=cursor.execute(q,(un,p)).fetchone()
    if userdata:
        print("welcome",userdata[0])
        print("1.all detail 2.update profile 3.change password 4.delete account")
        n=int(input("enter the choice"))
        if n==1:
            print("your detail:")
            print("your name: ",userdata[0])
            print("your username: ",userdata[1])
            print("your password: ",userdata[2])
            print("your mobile: ",userdata[3])
        elif n==2:
            print("1.name 2.mobile_no")
            n=int(input("enter your choice"))
            if n==1:
                newname=input('enter your newname')
                q='''update User set Name=? where Name=?'''
                cursor.execute(q,(newname,userdata[0]))
                conn.commit()
                print("name update")
            elif n==2:
                newmobile=input('enter your newmobile_no')
                q='''update User set mobile=? where mobile=?'''
                cursor.execute(q,(newmobile,userdata[3]))
                conn.commit()
                print("mobile_no update")

            else:
                print("wrong choice")
        elif n==3:
            oldpassword=input("enter your old password")
            if oldpassword==userdata[2]:
                newpassword=input('enter your new password')
                q='''update User set password=? where password=?'''
                cursor.execute(q,(newpassword,oldpassword))
                conn.commit()
                print("password changed")

            else:
                print("enter valid password")
        elif n==4:
            q='''delete from User where=?'''
            cursor.execute(q,(userdata[1]))
            conn.commit()
            print("account deleted")



    else:
        print("enter valid username and password")
    login()
def insert(name, username, password, mobile):
    insert_q = '''insert into User values(?,?,?,?)
    '''
    cursor.execute(insert_q,(name, username, password, mobile))
    conn.commit()
    print("your data is added for login enter username and password");
    login()

def Alluser():
    q = '''
         SELECT Username FROM User 
    '''
    data = cursor.execute(q).fetchall()
    return data

def signup():
    usernames = []
    data = Alluser()
    if data:
        for user in data:
            usernames.append(user[0])

    n = input("Enter your name")
    while True:
        un = input("Enter your Username")
        if un in usernames:
            print("This username is already exists. Try Another.")
        else:
            break
    p = input("enter your password")
    m = input("enter your mobile no.")
    insert(n,un,p,m)
    login()
print("1.signup  2.login")
n = int(input("enter the choice"))
if n == 1:
    signup()
elif n == 2:
    login()
else:
    print("wrong choice");


