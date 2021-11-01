import mysql.connector

con=mysql.connector.connect(
    host='bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com',
    user='u8lptery3cpdnz6z',
    password='shuFpc4qP9hMgrKn6har',
    database='bguauc6jvlo4oxas7z03'
)
curs=con.cursor()
curs.execute("alter table bookstoredb add review varchar(100)")
print("Column added sucessfully:)")
con.commit()
con.close()