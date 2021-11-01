import mysql.connector

con=mysql.connector.connect(
    host='bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com',
    user='u8lptery3cpdnz6z',
    password='shuFpc4qP9hMgrKn6har',
    database='bguauc6jvlo4oxas7z03'
)
curs=con.cursor()
try:
    auth=input("Enter Author name: ")
    pub=int(input("Enter Publication Year: "))
    curs.execute("select * from bookstoredb")
    data=curs.fetchall()
    for i in data:
        if i[2]==auth.lower() or i[4]==pub:
            print(i)
            
except:
    print('invalid value...')