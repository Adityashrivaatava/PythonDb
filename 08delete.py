import mysql.connector

con=mysql.connector.connect(
    host='bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com',
    user='u8lptery3cpdnz6z',
    password='shuFpc4qP9hMgrKn6har',
    database='bguauc6jvlo4oxas7z03'
)
curs=con.cursor()
bid=int(input("Enter bookid: "))
curs.execute("select * from bookstoredb where bookid=%d"%bid)
data=curs.fetchall()
if data:
    print(data)
    dele=input("Do you want to delete this book?(yes/no): ")
    if dele.lower()=="yes":
        curs.execute("delete from bookstoredb where bookid=%d"%bid)
        con.commit()
        print("Deleted Sucessfully:)")
    else:
        print("Not Deleting:)")
else:
    print("Book is not in database:(")