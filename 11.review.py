import mysql.connector

con=mysql.connector.connect(
    host='bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com',
    user='u8lptery3cpdnz6z',
    password='shuFpc4qP9hMgrKn6har',
    database='bguauc6jvlo4oxas7z03'
)
curs=con.cursor()
print("write review on books by bookid")
bid=int(input("Enter bookid: "))
rev=input("Enter review: ")
curs.execute("select bookid from bookstoredb where bookid=%d"%bid)
data=curs.fetchall()
if data:
    curs.execute("update bookstoredb set review='%s' where bookid=%d"%(rev,bid))
    con.commit()
    print("thanks for your review:)")
else:
    print("book not in database:(")
