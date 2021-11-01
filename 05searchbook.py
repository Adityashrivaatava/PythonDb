import mysql.connector

con=mysql.connector.connect(
    host="bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com",
    user="u8lptery3cpdnz6z",
    password="shuFpc4qP9hMgrKn6har",
    database="bguauc6jvlo4oxas7z03"
)

curs=con.cursor()
try:
    print("Search Book by Book id....")
    bid=int(input("Enter Book Id:"))
    curs.execute("select * from bookstoredb where bookid=%d"%bid)
    data=curs.fetchall()

    if data:
        print(data)
        print("Book found")
    else:
        print("Book Not Found:(")
except:
    print("Invalid Value....")