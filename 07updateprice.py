import mysql.connector

con=mysql.connector.connect(
    host='bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com',
    user='u8lptery3cpdnz6z',
    password='shuFpc4qP9hMgrKn6har',
    database='bguauc6jvlo4oxas7z03'
)

curs=con.cursor()
bid=int(input("Enter book code: "))
pri=int(input("Enter new price: "))

curs.execute("select bookid from bookstoredb where bookid=%d"%bid)
data=curs.fetchall()
if data:
    curs.execute("update bookstoredb set price=%d where bookid=%d"%(pri,bid))
    con.commit()
    print("price updated sucessfully:)")
else:
    print("book not found in database:(")