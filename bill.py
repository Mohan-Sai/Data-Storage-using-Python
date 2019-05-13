import sqlite3
conn=sqlite3.connect('bill.db')
c=conn.cursor()
bill={"Gulshan":9896621213,"Mohan":9160706262}
cust_name=input("enter the name")
cust_details={}

#Execute the below CREATE TABLE command only once. After the first time comment it out. Dont worry about how the other queries will work 
#if there is no table. Upon execution of below lines of code a .db is produced. All your queries work on it.
#c.execute("""CREATE TABLE customers(
#            Name varchar,
#            Phone_Number integer
#       )""")


c.execute("INSERT INTO customers VALUES('Sai',9160786262)")
#database using dictionary
def billing(name):
    if name in bill:
        print("Existing User")
    else:
        cust_num=input("Enter your phone number")
        bill[name]=cust_num
    print(bill)



#database using sqlite db
def billing1(name):
    c.execute("SELECT * FROM customers WHERE Name=(?)",(cust_name,))
    data=c.fetchall()
    print(data)
    print(len(data))
    if (len(data)!=0):
        print("Fuck off")
    else:
        cust_num=input("Enter your phone number")
        bill[name]=cust_num
        
        c.execute("INSERT INTO customers VALUES(:Name,:Phone_Number)",{'Name':cust_name,'Phone_Number':cust_num})
        c.execute("SELECT * FROM customers")
        print(c.fetchall())
        conn.commit()
        conn.close()

billing1(cust_name)
