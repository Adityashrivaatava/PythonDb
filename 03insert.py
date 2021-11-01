import mysql.connector
con=mysql.connector.connect(
    host="bguauc6jvlo4oxas7z03-mysql.services.clever-cloud.com",
    user="u8lptery3cpdnz6z",
    password="shuFpc4qP9hMgrKn6har",
    database="bguauc6jvlo4oxas7z03"
)
curs=con.cursor()
try:
    bid=int(input("Enter Book Id: "))
    bnm=input("Enter Book Name: ")
    aut=input("Enter Author Name: ")
    cat=input("Enter Category Of Book: ")
    pub=int(input("Enter Publication Year: "))
    pri=int(input("Enter Price Of The Book: "))


    curs.execute("insert into bookstoredb values(%d,'%s','%s','%s',%d,%d)"%(bid,bnm,aut,cat,pub,pri))
    con.commit()
    print("The Book inserted sucessfully:)")
except:
    print("invalid values....")

con.close()